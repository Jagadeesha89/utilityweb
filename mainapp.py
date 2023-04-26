import streamlit as st
from loan import loan_repay
from tax import tax_cal

page=st.sidebar.selectbox("Utility Services",("EMI Calculator","Tax Calculator"))

if page == "EMI Calculator":
    loan_repay()
else:
    tax_cal()