import pandas as pd
import numpy as np
import streamlit as st

def main():
    
    st.title("Welcome to Loan EMI Calculator")
    Loan=st.text_input("**Loan Amount**")
    Interest=st.text_input("**Enter Rate of Interest (without %)**")
    Tenor=st.text_input("**Number of months**")
    
    if Loan == "":
        print("You did not enter a number.")
    else:
        Loan = int(Loan)
    
    if Interest == "":
        print("You did not enter a number.")
    else:
        Interest = float(Interest)
    
    if Tenor == "":
        print("You did not enter a number.")
    else:
        Tenor = int(Tenor)
    
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
            repayment_schedule.append((i+1,monthly_payment,principal_paid,interest,balance))
        print("Payment\tBalance\tPrincipal\tInterest\tPayment")
        for i,(month,monthly_payment,principal_paid,interest,balance)in enumerate (repayment_schedule):
            print(f"{month}\t{monthly_payment:.2f}\t{principal_paid:.2f}\t{interest:.2f}\t{balance:.2f}")
           
            
        columns=['Month','Installment Amount','Principal Payment','Interest Payment','Principal Balance']
        df=pd.DataFrame(repayment_schedule,columns=columns)
        df=df.set_index('Month')
        df['Principal Balance'] = df['Principal Balance'].astype('int64')
        df['Principal Payment'] = df['Principal Payment'].astype('int64')
        df['Interest Payment'] = df['Interest Payment'].astype('int64')
        df['Installment Amount'] = df['Installment Amount'].astype('int64')

        
        st.subheader("Your Loan EMI Calculation Summary")
        
        st.write("***Your Loan Amount:***","Rs.",(f"{Loan}"),"/-")
        st.write("***Rate of Interest:***",(f"{Interest:.2f}"),"%")
        st.write("***Total Tenor :***",(f"{Tenor}"),"Months")
        st.write("***Total Interest Payable  :***","Rs.",(f"{df['Interest Payment'].sum()}"),"/-")
        st.write("***Monthly Installment :***","Rs.",(f"{round(monthly_payment)}"),"/-")
        
        st.subheader("Your Estimated Loan Repayment Schedule")
         
        result=st.dataframe(df)
        st.success(result)
        st.balloons()
        
if __name__=='__main__':
    main()
    
    