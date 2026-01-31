# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 19:21:03 2026

@author: ompha
"""

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Rabali Ompha | Profile",
    page_icon="🎓",
    layout="wide"
)

# ---------------- STYLE (ROUND IMAGE + ALIGNMENT) ----------------
st.markdown(
    """
    <style>
    .profile-img {
        border-radius: 50%;
        width: 120px;       /* smaller size */
        height: 120px;      /* square */
        object-fit: cover;  /* crop nicely */
        margin-right: 18px; /* space between image and text */
    }
    .profile-container {
        display: flex;
        align-items: center; /* vertical center with text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown(
    f"""
    <div class="profile-container">
        <img class="profile-img" src="https://raw.githubusercontent.com/MrOTheAnalyst/css_streamlit_2026/main/pic.jpeg">
        <div>
            <h1>Rabali Ompha</h1>
            <p>📧 <b>Email:</b> ompharabali9@gmail.com<br>
            🏫 <b>Institution:</b> Vaal University of Technology<br>
            🏢 <b>Department:</b> Engineering and Data Science<br>
            📍 <b>Location:</b> South Africa</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- TABS ----------------
tabs = st.tabs(["🔬 Research", "📊 Projects", "🎓 Education", "🏆 Awards", "📞 Contact"])

# ---------------- RESEARCH ----------------
with tabs[0]:
    st.header("Research Interests")
    st.markdown("""
- Production and Workflow analysis  
- Supply chain and Inventory management  
- Process optimization and efficiency improvement  
- Quality Control and Performance Measurement (KPIs)  
- Data analysis for operational and business decision-making  
- Data visualization and reporting using dashboards  
""")

# ---------------- PROJECTS ----------------
with tabs[1]:
    st.header("Projects")

    with st.expander("🚭 Smoking Health Risk Analysis – Power BI"):
        st.write(
            "Analyzed health risk factors associated with smoking using Power BI dashboards "
            "to support data-driven health insights."
        )

    with st.expander("💰 TapNext Finance Dashboard – Excel"):
        st.write(
            "Built an interactive financial dashboard in Excel to track performance, trends, "
            "and key financial indicators."
        )

# ---------------- EDUCATION ----------------
with tabs[2]:
    st.header("Education")
    st.markdown("""
🎓 **Diploma in Industrial Engineering**  
📍 Vaal University of Technology  
📅 *In progress*  
⏳ **Expected completion:** 2026  
""")

# ---------------- AWARDS ----------------
with tabs[3]:
    st.header("Awards & Certifications")
    st.markdown("""
- 🟡 Six Sigma White Belt  
- 📊 Certified Data Analytics – Cisco Networking Academy  
- 💻 Certified Data Science Tools:
  - Python  
  - R  
  - SQL  
  - Excel  
  - Tableau  
  - Power BI  
""")

# ---------------- CONTACT ----------------
with tabs[4]:
    st.header("Contact Information")
    st.markdown("""
📞 **Phone:** +27 76 128 5492  
📧 **Email:** ompharabali9@gmail.com  
""")

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Rabali Ompha | Streamlit Portfolio")


