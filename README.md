# 🌍 Life Expectancy Dashboard  
### **Big Data & AI — SRH University of Applied Sciences**

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📘 Overview

This interactive **Life Expectancy Dashboard** is a Big Data & AI project designed to analyze global health outcomes using WHO data. It transforms raw health and socioeconomic indicators into **interactive visual insights**, helping users compare countries, explore trends, and understand global development patterns.

Built with **Streamlit**, the dashboard provides clean UI, engineered KPIs, and country-level analytics for over 190 nations (2000–2015).

---

## ✨ Features

### 🏠 Landing Page
- Country-level KPIs  
- Life expectancy interpretation  
- Mortality & economic indicators  
- Government Health Expenditure (%)

### 📈 Trends & Comparisons
- Multi-country time-series  
- Health Index  
- Economic Index  
- Mortality Pressure  
- Scatterplot comparison

### 📊 Data Explorer
- Full dataset view  
- Sorting, filtering, CSV export  

### ℹ️ About Page
- Dataset details  
- KPI engineering  
- Beneficiaries  
- Future work  
- Credits  

---

## 🧠 Dataset Overview

Indicators include:
- Life Expectancy  
- Adult & Child Mortality  
- GDP per Capita  
- Schooling  
- BMI  
- Income Composition  
- Health Expenditure  

Dataset was cleaned:
✔ Thinness columns removed  
✔ Missing values handled  
✔ Normalized for KPI creation  

---

## ⚙️ KPI Engineering

### 1️⃣ Health Index
- Life Expectancy  
- BMI  
- Adult Mortality (inverse)  

### 2️⃣ Economic Index
- GDP  
- Income Composition  
- Schooling  

### 3️⃣ Mortality Pressure
- Adult Mortality  
- Infant Deaths  
- Under-5 Deaths  

---

## 📁 Project Structure

```
Life-Expectancy-Dashboard/
├─ Overview.py
├─ pages/
│  ├─ 01_Trends_and_Comparison.py
│  ├─ 02_Data_Explorer.py
│  └─ 03_About.py
├─ data/
│  └─ LifeExpectancyData_CLEANED.csv
├─ .streamlit/
│  └─ config.toml
├─ requirements.txt
└─ README.md
```

---

## 🔧 Installation

```bash
git clone https://github.com/YOUR-USERNAME/Life-Expectancy-Dashboard.git
cd Life-Expectancy-Dashboard
python -m venv .venv
source .venv/bin/activate  # or .venv/Scripts/Activate.ps1 on Windows
pip install -r requirements.txt
streamlit run Overview.py
```

---

## 👥 Who Benefits?

- Public health agencies  
- Policy makers  
- Development economists  
- UN / WHO / UNICEF  
- Researchers & data scientists  
- Students & educators  

---

## 🚀 Future Work

- Forecasting (ARIMA, Prophet, LSTM)  
- Regional deep-dives  
- Clustering countries  
- Policy simulation  
- More health indicators  
- AI-driven narrative insights  

---

## 📚 Credits

**Data Sources**
- WHO Global Health Observatory  
- Kaggle WHO Dataset  

**Technologies**
- Python  
- Streamlit  
- Plotly  
