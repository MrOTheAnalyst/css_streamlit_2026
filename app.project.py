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

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Rounded profile image */
img {
    border-radius: 50%;
}

/* Colored tabs */
[role="tab"] {
    background-color: #f0f2f6 !important;
    color: #333 !important;
    font-weight: bold;
}
[role="tab"]:hover {
    background-color: #d0e1ff !important;
}

/* Hover effect for expanders */
div[data-baseweb="accordion"] > div:hover {
    background-color: #f9f9f9;
    border-left: 4px solid #4a90e2;
    transition: 0.3s;
}

/* Section background */
section.main {
    background-color: #fcfcfc;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "https://raw.githubusercontent.com/MrOTheAnalyst/css_streamlit_2026/main/pic.jpeg",
        width=180
    )

with col2:
    st.title("Rabali Ompha")
    # Using HTML <br> for proper line breaks
    st.markdown("""
📧 <b>Email:</b> <a href="mailto:ompharabali9@gmail.com">ompharabali9@gmail.com</a><br>
🏫 <b>Institution:</b> Vaal University of Technology<br>
🏢 <b>Faculty:</b> Engineering<br>
📍 <b>Location:</b> South Africa
""", unsafe_allow_html=True)

st.divider()

# ---------------- TABS ----------------
tabs = st.tabs(["🔬 Research", "📊 Projects", "🎓 Education", "🏆 Awards", "📞 Contact"])

# ---------------- RESEARCH ----------------
with tabs[0]:
    st.header("Research Interests")
    st.markdown("""
- 🏭 Production and Workflow analysis  
- 📦 Supply chain and Inventory management  
- ⚙️ Process optimization and efficiency improvement  
- 📊 Quality Control and Performance Measurement (KPIs)  
- 📈 Data analysis for operational and business decision-making  
- 📉 Data visualization and reporting using dashboards  
""")

# ---------------- PROJECTS ----------------
with tabs[1]:
    st.header("Projects")

    with st.expander("🚭 Smoking Health Risk Analysis – Power BI"):
        st.write(
            "Analyzed health risk factors associated with smoking using Power BI dashboards "
            "to support data-driven health insights."
        )
        st.markdown("[View Power BI Dashboard](https://1drv.ms/u/c/e1abadb451e0b347/IQDOsehRgX6pSYtEJo50RQ-pAczc72mHR7oUgi-0S46WGmg?e=UrCA65)")

    with st.expander("👕 Sleak & Co Dashboard - Excel"):
        st.write(
            "Built an interactive dashboard to track clothing sales, inventory, and key business trends."
        )
        st.markdown("[View Excel Dashboard](https://1drv.ms/x/c/e1abadb451e0b347/IQA4erERPT_NRrE-rAR_KlwQAcPcc8mBGws6kvneZZUlNDg?e=ddyf3D)")

# ---------------- EDUCATION ----------------
with tabs[2]:
    st.header("Education")
    st.markdown("""
🎓 **Diploma in Industrial Engineering**  
📍 Vaal University of Technology  
📅 *In progress*  
⏳ **Expected completion:** 2026  
""")

# ---------------- AWARDS & CERTIFICATIONS ----------------
with tabs[3]:
    st.header("Awards & Certifications")
    st.markdown("""
- 🟡 Six Sigma White Belt  
- 📊 Certified Data Analytics – Cisco Networking Academy  
- 💻 Certified Data Science Tools - IBM:
  - Python  
  - R  
  - SQL  
  - Excel  
  - Tableau  
  - Power BI  
  - Data Science Fundamentals (Short Course)  
""")

# ---------------- CONTACT ----------------
with tabs[4]:
    st.header("Contact Information")
    st.markdown("""
📞 **Phone:** [+27 76 128 5492](tel:+27761285492)  
📧 **Email:** [ompharabali9@gmail.com](mailto:ompharabali9@gmail.com)  
""")
    st.button("Send Email", key="email_button")  # Optional interactive button

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Rabali Ompha | Streamlit Portfolio")


# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Rabali Ompha | Streamlit Portfolio")

