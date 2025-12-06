import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

# ============================================================
#               GLOBAL STYLING (MATCHES MAIN THEME)
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif !important;
}
.about-title {
    text-align: center; 
    font-weight: 700; 
    font-size: 2.2rem; 
    margin-bottom: -5px;
}
.section-title {
    font-weight: 700; 
    font-size: 1.35rem;
    margin-top: 25px;
}
.text-block {
    font-size: 1.05rem; 
    opacity: 0.9;
    line-height: 1.55rem;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
#                      ABOUT PAGE CONTENT
# ============================================================

st.markdown("<div class='about-title'>About This Dashboard</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='text-block'>
This interactive dashboard was developed as part of the <b>Big Data & Artificial Intelligence</b> module at 
<b>SRH University of Applied Sciences</b>. It explores global <b>life expectancy</b> trends using official WHO data, 
enriched by socioeconomic indicators such as GDP, schooling, mortality rates, and healthcare metrics.

The goal of this project is to demonstrate how <b>data engineering</b>, <b>statistical analysis</b>, and 
<b>interactive visualization</b> can provide meaningful insights into global health outcomes.
</div>
""", unsafe_allow_html=True)



# ============================================================
#                        DATASET SECTION
# ============================================================

st.markdown("<div class='section-title'>🌍 Dataset Overview</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
The dashboard is built on the <b>WHO Life Expectancy Dataset</b>, which includes annual data for 
<b>over 190 countries</b> between <b>2000 and 2015</b>.  
It covers a diverse set of indicators:

<ul>
<li><b>Life Expectancy</b> – average lifespan at birth</li>
<li><b>Adult Mortality</b> – probability of dying between age 15–60</li>
<li><b>Infant & Under-5 Deaths</b> – crucial child health indicators</li>
<li><b>GDP per Capita</b> – economic strength measure</li>
<li><b>Schooling</b> – average years of education</li>
<li><b>BMI</b> – nutritional metric</li>
<li><b>Income Composition of Resources</b> – inequality & human development proxy</li>
<li><b>Health Expenditure</b> – % of GDP spent on healthcare</li>
</ul>

The dataset was cleaned by standardizing column names, removing unrelated <i>thinness</i> columns, 
handling missing values, and ensuring all numerical fields were usable for statistical analysis.
</div>
""", unsafe_allow_html=True)



# ============================================================
#                        KPI SECTION
# ============================================================

st.markdown("<div class='section-title'>📊 KPI Engineering</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
Three composite KPIs were created to simplify complex health indicators into meaningful, comparable scores:

<b>1. Health Index</b>  
A combined measure of health quality, based on:
<ul>
<li>Life Expectancy (normalized)</li>
<li>BMI (normalized)</li>
<li>Adult Mortality (inverse normalized)</li>
</ul>

<b>2. Economic Index</b>  
Represents national development using:
<ul>
<li>GDP per Capita</li>
<li>Income Composition of Resources</li>
<li>Schooling</li>
</ul>

<b>3. Mortality Pressure</b>  
Captures overall mortality burden:
<ul>
<li>Adult Mortality</li>
<li>Infant Deaths</li>
<li>Under-Five Deaths</li>
</ul>

Each index uses <b>min–max normalization</b> to ensure fair comparison across variables
with different scales.
</div>
""", unsafe_allow_html=True)



# ============================================================
#                        DASHBOARD STRUCTURE
# ============================================================

st.markdown("<div class='section-title'>🖥️ Dashboard Structure</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
The dashboard consists of multiple interactive pages, designed for clarity and ease of exploration:

<ul>
<li><b>Landing Page</b> — A country snapshot with KPIs, trends, and a global interpretation.</li>
<li><b>Trends & Comparison</b> — Year-wise visual trends, GDP correlations, and top/bottom country rankings.</li>
<li><b>Data Explorer</b> — Offers full table exploration, filtering, and CSV export.</li>
<li><b>About</b> — Methodology, dataset description, and project rationale.</li>
</ul>

The user interface is styled with a <b>custom dark theme</b>, <b>Inter font</b>, centered layouts,
clean card design, and professional visual consistency across all pages.
</div>
""", unsafe_allow_html=True)



# ============================================================
#                        ANALYSIS GOALS
# ============================================================

st.markdown("<div class='section-title'>🎯 Project Goals</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
This project aims to:

<ul>
<li>Identify global drivers of life expectancy</li>
<li>Observe regional disparities between nations</li>
<li>Compare developed vs developing countries</li>
<li>Determine strongest correlations with lifespan</li>
<li>Provide an actionable, research-friendly dashboard</li>
</ul>

Ultimately, this dashboard demonstrates how <b>Big Data analytics</b> and 
<b>interactive applications</b> can support evidence-based decision-making 
in public health and global development.
</div>
""", unsafe_allow_html=True)


# ============================================================
#                 WHO BENEFITS FROM THIS DASHBOARD
# ============================================================

st.markdown("<div class='section-title'>🌍 Who Can Benefit From This Dashboard?</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
This dashboard provides value to a wide range of stakeholders, each using the insights for 
different decision-making and research purposes:

<ul>
<li><b>Public Health Agencies</b> — Track global health trends, mortality burdens, and areas requiring intervention.</li>

<li><b>Government Policy Makers</b> — Evaluate how economic development, education, and spending decisions 
impact national health outcomes.</li>

<li><b>Healthcare Planners</b> — Identify regions with high mortality pressure or low health indices to allocate 
resources more effectively.</li>

<li><b>Development Economists</b> — Study relationships between GDP, schooling, income distribution, and health outcomes.</li>

<li><b>Researchers & Data Scientists</b> — Explore correlations, derive statistical models, and build predictive 
analysis frameworks on global health data.</li>

<li><b>International Organizations (WHO, UN, UNICEF)</b> — Use KPI trends to monitor global well-being and 
compare country progress over time.</li>

<li><b>Students & Educators</b> — Access a clean, easy-to-understand visualization tool for learning global health 
analytics and big data techniques.</li>
</ul>

By translating raw WHO metrics into meaningful, interactive insights, this dashboard empowers stakeholders 
across public health, economics, policy, and academia.
</div>
""", unsafe_allow_html=True)


# ============================================================
#                        FUTURE WORK
# ============================================================

st.markdown("<div class='section-title'>🚀 Future Work</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>
While this dashboard provides meaningful insights into global health and development, several enhancements 
can further expand its analytical capabilities:

<ul>
<li><b>Time-Series Forecasting</b> — Implement predictive models (ARIMA, Prophet, LSTM) to estimate future 
life expectancy trends for each country.</li>

<li><b>Clustering & Segmentation</b> — Use machine learning methods such as K-means or hierarchical clustering 
to group countries based on health, mortality, and economic indicators.</li>

<li><b>Regional Deep-Dive</b> — Add continent- or region-level comparative dashboards to analyze disparities and 
spot geographic health patterns.</li>

<li><b>Additional Health Metrics</b> — Incorporate external datasets, such as immunization rates, nutrition indices, 
disease prevalence, or healthcare accessibility metrics.</li>

<li><b>Enhanced Data Quality</b> — Integrate official GDP series, World Bank development indicators, or UN 
human development metrics for improved accuracy and robustness.</li>

<li><b>Policy Simulation</b> — Build hypothetical “what-if” scenarios, such as how increasing healthcare spending 
or improving schooling might impact a country’s life expectancy.</li>

<li><b>Interactive Storytelling</b> — Add insights-driven narratives powered by AI to help users interpret 
complex relationships and trends more easily.</li>
</ul>

These ideas offer a roadmap for expanding this academic project into a more comprehensive tool for research, 
analytics, and policy planning.
</div>
""", unsafe_allow_html=True)



# ============================================================
#                        CREDITS
# ============================================================

st.markdown("<div class='section-title'>📚 Credits & References</div>", unsafe_allow_html=True)
st.markdown("""
<div class='text-block'>

<b>Data Sources:</b>
<ul>
<li>
    <a href="https://www.who.int/data/gho" target="_blank">
        World Health Organization (WHO) — Global Health Observatory
    </a>
</li>

<li>
    <a href="https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who" target="_blank">
        Kaggle Source Dataset — Life Expectancy WHO
    </a>
</li>
</ul>

<b>Tools & Libraries:</b>
<ul>
<li>Python (Pandas, NumPy, Matplotlib, Seaborn)</li>
<li>Streamlit for dashboard development</li>
<li>Plotly for interactive visualizations</li>
</ul>

<br>

<b>Developed By:</b><br>
<a href="https://www.linkedin.com/in/aakash-vashist-403b83281/" target="_blank">
    <b>Aakash Vashist</b>
</a><br>
M.Sc. Computer Science (Big Data & AI)<br>
SRH University of Applied Sciences, Leipzig, Germany

</div>
""", unsafe_allow_html=True)


