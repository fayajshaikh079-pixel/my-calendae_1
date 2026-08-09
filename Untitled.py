
import calendar 
import streamlit as st 
year = st.number_input("ENTER YEAR :", value=2026, step=1)
mont = st.number_input("enter month:",min_value=1, max_value=12, value=8)

st.text(calendar.mont(int(year),int (mont)))




