import pandas as pd
import numpy as np
import streamlit as st

def main():
    
    st.title("Welcome to Loan repayment schedule Genration")
    Loan=int(st.text_input("Loan amount"))
    Interest=float(st.text_input("Rate of Interest"))
    Tenor=int(st.text_input("Number of months"))
    result=""
    genrate=st.button("Genrate Repayment Schedule")
    if genrate:
        monthly_rate=(Interest/100)/12 
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
            
        columns=['Month','Principal Balance','Principal Payment','Interest Payment','Installment Amount']
        df=pd.DataFrame(repayment_schedule,columns=columns)
        df=df.set_index('Month')
        df['Principal Balance'] = df['Principal Balance'].astype('int64')
        df['Principal Payment'] = df['Principal Payment'].astype('int64')
        df['Interest Payment'] = df['Interest Payment'].astype('int64')
        df['Installment Amount'] = df['Installment Amount'].astype('int64')

        result=st.table(df)
        st.success(result)
        
        
if __name__=='__main__':
    main()
    
    