
import calendar 
import streamlit as st 
year = st.number_input("ENTER YEAR :", value=2026, step=1)
month = st.number_input("enter month:",min_value=1, max_value=12, value=8)

st.text(calendar.month(int(year),int (month)))




