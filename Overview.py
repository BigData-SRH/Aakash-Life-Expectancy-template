import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ===============================================================
#  GLOBAL STYLING (FONTS, DARK THEME, KPI CARDS, CENTERING)
# ===============================================================

st.set_page_config(page_title="Life Expectancy Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* Headings */
h1, h2, h3, h4 {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
}

/* KPI Cards */
.kpi-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 14px;
    backdrop-filter: blur(6px);
}

.kpi-title {
    font-size: 0.9rem;
    opacity: 0.85;
    margin-bottom: 4px;
}

.kpi-value {
    font-size: 1.7rem;
    font-weight: 700;
}

/* Centered title */
.centered {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ===============================================================
#  BACKEND (LOCAL TO THIS FILE — NO IMPORTS FROM OTHER PAGES)
# ===============================================================

def load_clean_data():
    df = pd.read_csv("data/LifeExpectancyData_CLEANED.csv")

    df.columns = (
        df.columns
        .str.replace("\xa0", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df = df.loc[:, ~df.columns.duplicated()].copy()

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    for col in df.select_dtypes(include=["number"]).columns:
        df[col].replace([np.inf, -np.inf], np.nan, inplace=True)

    df.fillna(df.median(numeric_only=True), inplace=True)
    return df


def detect_col(df, keywords):
    hits = []
    for col in df.columns:
        norm = col.lower().replace(" ", "").replace("_", "")
        if all(k in norm for k in keywords):
            hits.append(col)
    return sorted(hits, key=len)[0] if hits else None


def min_max(series):
    series = pd.to_numeric(series, errors="coerce")
    mn, mx = series.min(), series.max()
    if pd.isna(mn) or pd.isna(mx) or mn == mx:
        return pd.Series([0.5] * len(series), index=series.index)
    return (series - mn) / (mx - mn)


def safe_value(row, colname):
    try:
        return float(row[colname])
    except:
        return float(pd.to_numeric(row[colname].iloc[0]))


def add_kpis(df):
    df = df.copy()

    col_life   = detect_col(df, ["life", "expect"])
    col_gdp    = detect_col(df, ["gdp"])
    col_adult  = detect_col(df, ["adult", "mort"])
    col_u5     = detect_col(df, ["under", "five"])
    col_sch    = detect_col(df, ["school"])

    # store detected column names for use in pages
    df["_life"]  = col_life
    df["_gdp"]   = col_gdp
    df["_adult"] = col_adult
    df["_u5"]    = col_u5
    df["_sch"]   = col_sch

    return df


# ===============================================================
#                        LOAD DATA
# ===============================================================

df = add_kpis(load_clean_data())

life_col  = df["_life"].iloc[0]
gdp_col   = df["_gdp"].iloc[0]
adult_col = df["_adult"].iloc[0]
u5_col    = df["_u5"].iloc[0]
sch_col   = df["_sch"].iloc[0]


# ===============================================================
#           CENTERED TITLE + SUBTITLE
# ===============================================================

st.markdown("""
<div class="centered" style="padding-top: 5px;">
    <h1 style="font-weight: 700;">Life Expectancy Dashboard</h1>
    <p style="font-size: 1.05rem; opacity: 0.85;">
        A minimal, research-focused Big Data & AI analysis based on WHO life expectancy data.
    </p>
</div>
""", unsafe_allow_html=True)


# ===============================================================
#                   CENTERED DROPDOWNS
# ===============================================================

c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    colA, colB = st.columns(2)

    with colA:
        selected_year = st.selectbox("**Select Year**", sorted(df["Year"].unique()))

    with colB:
        selected_country = st.selectbox("**Select Country**", sorted(df["Country"].unique()))


# ===============================================================
#                 COUNTRY SNAPSHOT SECTION
# ===============================================================

row = df[(df["Country"] == selected_country) & (df["Year"] == selected_year)].iloc[0]

st.markdown(f"## Country Snapshot — {selected_country} ({selected_year})")

# ------------------------
# ROW 1 — Life, Schooling, GDP
# ------------------------
g1, g2, g3 = st.columns(3)

with g1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🌱 Life Expectancy (years)</div>
        <div class="kpi-value">{row[life_col]:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with g2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📘 Schooling (years)</div>
        <div class="kpi-value">{row[sch_col]:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with g3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💰 GDP per Capita (USD)</div>
        <div class="kpi-value">{int(row[gdp_col]):,}</div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------
# ROW 2 — Mortality + Health Expenditure
# ------------------------
h1, h2, h3 = st.columns(3)

with h1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⚰️ Adult Mortality (per 1000)</div>
        <div class="kpi-value">{row[adult_col]:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with h2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🧸 Under-5 Mortality (per 1000)</div>
        <div class="kpi-value">{row[u5_col]:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with h3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🏥 Gov Health Expenditure (%)</div>
        <div class="kpi-value">{row['percentage expenditure']:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)



# ===============================================================
#              HIGH-LEVEL INTERPRETATION
# ===============================================================

st.markdown("## High-level Interpretation")

global_avg = round(df[life_col].mean(), 1)
life_val = row[life_col]

msg_color = "🟢" if life_val > global_avg else "🟡"

st.markdown(
    f"""
<div style="background: rgba(255,255,255,0.06); padding: 18px; border-radius: 12px;">
    {msg_color} In {selected_year}, <b>{selected_country}</b> has a life expectancy of 
    <b>{life_val} years</b>, compared to the global average of <b>{global_avg} years</b>.
</div>
""",
    unsafe_allow_html=True,
)
