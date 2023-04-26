import pandas as pd
import numpy as np
import streamlit as st




def tax_cal():
    st.title("Welcome to Tax Calculator")
    income=st.text_input("Total taxable income (Rs)")
    ded_1=st.text_input("Deduction under 80c")
    ded_2=st.text_input("Interest on Home Loan")
    ded_3=st.text_input("Any other exemptions and deduction")
    
    if income == "":
        print("You did not enter a number.")
    else:
        income = int(income)
    
    if ded_1 == "":
        print("You did not enter a number.")
    else:
        ded_1 = int(ded_1)
    
    if ded_2 == "":
        print ("You did not enter a number.")
    else:
        ded_2 = int(ded_2)
    
    if ded_3 == "":
        print ("You did not enter a number.")
    else:
        ded_3=int(ded_3)
    
    st.write("*If deduction & exemptions is nil please enter zero*")    
    
    def old_tax_cal(income_1):
        if income_1 <= 500000:
            return 0
        elif income_1 <=250000:
            tax=0
        elif income_1 <= 500000:
            tax=(income_1 -250000) * 0.05
        elif income_1 <=1000000:
            tax=12500 +(income_1 - 500000) * 0.2
        else:
            tax=112500 + (income_1 - 1000000)*0.3
        return tax

    def new_tax_cal(income):
        if income <750000:
            return 0
        elif income <=300000:
            tax= 0
        elif income <= 600000:
            tax=(income -300000) * 0.05
        elif income <= 900000:
            tax=15000 + (income -600000)* 0.1
        elif income <=1200000:
            tax=45000 + (income - 900000) * 0.15
        elif income <= 1500000:
            tax=90000 + (income - 1200000) * 0.2
        else:
            tax=150000 + (income - 1500000) * 0.3
        return tax        
        
    ok=st.button("Calculate Tax")
    if ok:    
        deduction=(ded_1+ded_2+ded_3)
        if deduction == "":
            print("enter")
        else:
            deduction=int(deduction)
            
        stan_dedcu=50000
        income_1=income - deduction - stan_dedcu
        income=income-stan_dedcu
    
        old_tax=old_tax_cal(income_1) 
        new_tax=new_tax_cal(income)

        if old_tax == "":
            print("enter")
        else:
            old_tax=int(old_tax)
        
        if new_tax == "":
            print('enter')
        else:
            new_tax=int(new_tax)
            
        b_tax=income-stan_dedcu-deduction
        n_tax=income-stan_dedcu
            
        final_old_tax=(old_tax * 0.04) 
        final_new_tax=(new_tax * 0.04) 
        
        final_old_tax_1=final_old_tax + old_tax
        final_new_tax_1=final_new_tax + new_tax
        
        a=final_old_tax_1 - final_new_tax_1
        b=final_new_tax_1 - final_old_tax_1
        
        st.subheader("Your Tax Calculation Suammary")
        
        df=pd.DataFrame({"Particulars":['Total Taxable Income','Total Dedcutions','Standard Deduction','Final Taxable incme','Tax Amount before Cess','Cess (%)','Final Tax Amount'],
                         "New Tax Regim":[income,"No Deduction",stan_dedcu,n_tax,new_tax,"4%",final_new_tax_1],
                         "Old Tax Regim":[income,deduction,stan_dedcu,b_tax,old_tax,"4%",final_old_tax_1]})
        
        st.table(df)
        
       
        
        if final_old_tax_1 > final_new_tax_1:
           st.write ("***Old Tax Regim having higher tax laiblity","," "if you opted for New Tax Regim you will save Rs.***",(f"{a}"),"/-")
        else:
            st.write("***New Tax Regim higher higher tax laiblity","," "if you opted for Old Tax Regim you will save Rs.***",(f"{b}"),"/-")
    
if __name__=='__tax_cal__':
    tax_cal()
