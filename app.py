import pandas as pd
import numpy as np
import streamlit as st

st.title("Welcome to Loan repayment schedule Genration")
Loan=int(st.number_input("Loan amount"))
Interest=float(st.number_input("Rate of Interest"))
Tenor=int(st.number_input("Number of months"))

monthly_rate=(Interest/100)/12 

# calculate the monthly EMI amount
monthly_payment=(monthly_rate*Loan)/(1-(1 + monthly_rate)**(-Tenor))
repayment_schedule=[]
balance=Loan
for i in range(Tenor):
    interest=monthly_rate*balance
    principal_paid=monthly_payment - interest
    balance -= principal_paid
    repayment_schedule.append((i+1,balance,principal_paid,interest,monthly_payment)) 
                              
print("Payment\tBalance\tPrincipal\tInterest\tPayment")
for i,(month,balance,principal_paid,interest,monthly_payment)in enumerate (repayment_schedule):
    print(f"{month}\t{balance:.2f}\t{principal_paid:.2f}\t{interest:.2f}\t{monthly_payment:.2f}")
    
#columns=['month','principal','prin','int','Install']
#df=pd.DataFrame(repayment_schedule,columns=columns)

df=repayment_schedule

button=st.button("Genrate")

if button:
    pred=df
    print(pred)
    
    
    st.subheader(pred)
