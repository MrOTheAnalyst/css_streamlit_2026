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

# ---------------- STYLE (ROUND IMAGE) ----------------
st.markdown(
    """
    <style>
    img {
        border-radius: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "https://drive.google.com/file/d/1JniRX9ySyvoT_6qXdS26xfk4-khjvTB1/view?usp=sharing",
        width=180
    )

with col2:
    st.title("Rabali Ompha")
    st.markdown("""
📧 **Email:** ompharabali9@gmail.com  
🏫 **Institution:** Vaal University of Technology  
🏢 **Department:** Engineering and Data Science  
📍 **Location:** South Africa  
""")

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


