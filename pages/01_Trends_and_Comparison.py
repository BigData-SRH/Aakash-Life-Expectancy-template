import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trends & Comparisons", page_icon="📈", layout="wide")

# -------------------------------------------------------
# REUSE THE SAME LOGIC AS app.py (NO IMPORTS!)
# -------------------------------------------------------

def detect_col(df, keys):
    for col in df.columns:
        norm = col.lower().replace(" ", "").replace("-", "")
        if all(k in norm for k in keys):
            return col
    return None

def min_max(series):
    s = pd.to_numeric(series, errors="coerce")
    mn, mx = s.min(), s.max()
    if mn == mx:
        return pd.Series(0.5, index=s.index)
    return (s - mn) / (mx - mn)

@st.cache_data
def load_and_prepare():
    df = pd.read_csv("data/LifeExpectancyData_CLEANED.csv")
    df.columns = df.columns.str.replace("\xa0", " ", regex=True).str.strip()

    # Detect columns
    life   = detect_col(df, ["life","expect"])
    bmi    = detect_col(df, ["bmi"])
    adult  = detect_col(df, ["adult","mort"])
    infant = detect_col(df, ["infant","death"])
    under5 = detect_col(df, ["under","five"])
    gdp    = detect_col(df, ["gdp"])
    income = detect_col(df, ["income","composition"])
    school = detect_col(df, ["school"])

    # KPIs
    df["Health_Index"] = (
        min_max(df[life]) +
        min_max(df[bmi]) +
        (1 - min_max(df[adult]))
    ) / 3

    df["Economic_Index"] = (
        min_max(df[gdp]) +
        min_max(df[income]) +
        min_max(df[school])
    ) / 3

    df["Mortality_Pressure"] = (
        min_max(df[adult]) +
        min_max(df[infant]) +
        min_max(df[under5])
    ) / 3

    return df, life, gdp

df, LIFE_COL, GDP_COL = load_and_prepare()

# -------------------------------------------------------
# UI — CLEAN MINIMAL ACADEMIC DARK THEME
# -------------------------------------------------------
st.title("📈 Trends & Country Comparisons")

years = sorted(df["Year"].unique())
countries = sorted(df["Country"].unique())

col1, col2 = st.columns([1.2, 1.2])

with col1:
    year_start, year_end = st.select_slider(
        "Select Year Range",
        options=years,
        value=(years[0], years[-1])
    )

with col2:
    selected_countries = st.multiselect(
        "Select Countries",
        countries,
        default=countries[:3]
    )

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

# Filter by selection
mask = (df["Year"] >= year_start) & (df["Year"] <= year_end)
df_sel = df[mask & df["Country"].isin(selected_countries)]

# -------------------------------------------------------
# 1) LIFE EXPECTANCY TRENDS
# -------------------------------------------------------
st.subheader("Life Expectancy Trends")

fig_life = px.line(
    df_sel,
    x="Year",
    y=LIFE_COL,
    color="Country",
    markers=True,
    template="plotly_dark",
    title="Life Expectancy Over Time"
)

st.plotly_chart(fig_life, use_container_width=True)

# -------------------------------------------------------
# 2) COMPOSITE KPI TRENDS
# -------------------------------------------------------
st.subheader("Composite Index Trends")

tab1, tab2, tab3 = st.tabs(["Health Index", "Economic Index", "Mortality Pressure"])

with tab1:
    fig_h = px.line(
        df_sel,
        x="Year",
        y="Health_Index",
        color="Country",
        template="plotly_dark"
    )
    st.plotly_chart(fig_h, use_container_width=True)

with tab2:
    fig_e = px.line(
        df_sel,
        x="Year",
        y="Economic_Index",
        color="Country",
        template="plotly_dark"
    )
    st.plotly_chart(fig_e, use_container_width=True)

with tab3:
    fig_m = px.line(
        df_sel,
        x="Year",
        y="Mortality_Pressure",
        color="Country",
        template="plotly_dark"
    )
    st.plotly_chart(fig_m, use_container_width=True)

# -------------------------------------------------------
# 3) HEALTH vs ECONOMIC STRENGTH
# -------------------------------------------------------
st.subheader("Health vs Economic Strength")

year_for_plot = st.selectbox(
    "Select Year for Scatter",
    years,
    index=len(years)-1
)

df_scatter = df[(df["Year"] == year_for_plot) & (df["Country"].isin(selected_countries))]

fig_scatter = px.scatter(
    df_scatter,
    x="Economic_Index",
    y="Health_Index",
    color="Country",
    size=GDP_COL,
    size_max=25,
    template="plotly_dark",
    title=f"Health vs Economic Index — {year_for_plot}",
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("""
**Interpretation:**  
- Countries in the **top-right** quadrant are both *wealthy and healthy*.  
- **Bottom-right:** Economically strong but struggling with health outcomes.  
- **Top-left:** Good health outcomes despite lower economic strength.  
""")
