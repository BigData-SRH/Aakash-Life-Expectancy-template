import streamlit as st
import pandas as pd
import numpy as np

# ===============================================================
#     LOCAL BACKEND (MATCHES SAME BACKEND AS TRENDS PAGE)
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


# ===============================================================
#                       PAGE STARTS HERE
# ===============================================================

st.set_page_config(page_title="Data Explorer", page_icon="📊", layout="wide")
st.title("📊 Data Explorer")

df = load_clean_data()

countries = ["All"] + sorted(df["Country"].unique())
years     = ["All"] + sorted(df["Year"].unique().tolist())

c1, c2 = st.columns(2)
with c1:
    selected_country = st.selectbox("Country", countries)
with c2:
    selected_year = st.selectbox("Year", years)

filtered = df.copy()

if selected_country != "All":
    filtered = filtered[filtered["Country"] == selected_country]

if selected_year != "All":
    filtered = filtered[filtered["Year"] == selected_year]

st.dataframe(filtered, use_container_width=True, height=450)

# Download option
st.download_button(
    "Download Filtered CSV",
    filtered.to_csv(index=False).encode(),
    "filtered_data.csv",
    "text/csv"
)
