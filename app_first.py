# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 10:59:03 2026

@author: ompha
"""

import streamlit as st

st.write("CSS 2026 :)")

st.write("day3")

st.title("My first Sreamlit App")

number = st.slider("pick a number", 1, 100)

st.write(f"you picked {number}")