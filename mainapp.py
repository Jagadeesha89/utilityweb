import streamlit as st
import pandas as pd
import numpy as np
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login
import time






ti=st.title("Welcome to Utility Services")
page=st.selectbox("List of Services",("Select","AI Powered Chat GPT","EMI Calculator","Tax Calculator"))


def main():
    def tax_cal():
        st.title("Tax Calculator")
        income=st.text_input("**Total Income (Rs)**")
        ded_1=st.text_input("**Deduction under 80c**",0)
        ded_2=st.text_input("**Interest on Home Loan**",0)
        ded_3=st.text_input("**Any other exemptions and deduction**",0)
    
        if income == "":
            print ("You did not enter a number.")
        else:
            income = int(income)
    
        if ded_1 == "":
            print ("You did not enter a number.")
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
            if income <700000:
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
            income_2=income-stan_dedcu
    
            old_tax=old_tax_cal(income_1) 
            new_tax=new_tax_cal(income_2)

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
        
            df=pd.DataFrame({"Particulars":['Total Income','Total Dedcutions','Standard Deduction','Final Taxable incme','Tax Amount before Cess','Cess (%)','Final Tax Amount'],
                         "New Tax Regim":[income,0,stan_dedcu,n_tax,new_tax,"4",final_new_tax_1],
                         "Old Tax Regim":[income,deduction,stan_dedcu,b_tax,old_tax,"4",final_old_tax_1]})
        
            df=df.set_index("Particulars")
    
        
            st.table(df)
   
        
       
        
            if final_old_tax_1 > final_new_tax_1:
                st.write ("***Old Tax Regim having higher tax laiblity","," "if you opted for New Tax Regim you will save Rs.***",(f"{a}"),"/-")
            elif final_old_tax_1 == final_new_tax_1:
                st.write("***Old Tax Regim and New Tax Regim having same tax laiblity","," "You can opt for any regim depend on the Deduction***")
            else:
                st.write("***New Tax Regim having higher tax laiblity","," "if you opted for Old Tax Regim you will save Rs.***",(f"{b}"),"/-")
           
       
           
    def loan_repay():
    
        st.title("Loan EMI Calculator")
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
         
            st.dataframe(df)
        
    def chatbot():
        st.title("AI powered Chat GPT")
        st.markdown('''
         - This app is an LLM-powered chatbot built using,HugChat
         - This may produce inacurate information about people, places, or facts
         - Limited knowledge of world and events after 2021
         
         
         💡 Note: No API key required!
         ''')
            
        ## generated stores AI generated responses
        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["I'm AI powered Chat GPT, How may I help you?"]
        ## past stores User's questions
        if 'past' not in st.session_state:
            st.session_state['past'] = ['Hello!']

       
        # User input
        
            
        ## Function for taking user provided prompt as input
        with st.form("chat_input", clear_on_submit=True):
             a, b = st.columns([4, 1])
             user_input = a.text_input(
                  label="Your message:",
                  placeholder="What would you like to say?",
                  label_visibility="collapsed",
             )
        b.form_submit_button("Send", use_container_width=True)
       
     # Layout of input/response containers
        input_container = st.container()
        colored_header(label='', description='', color_name='blue-30')
        response_container = st.container()

        ## Applying the user input box
        with input_container:
            user_input_a = a
            
        
        # Log in to huggingface and grant authorization to huggingchat
        email="jaga.m.gowda@gmail.com"
        passwd="Jaga@9731"
        sign = Login(email, passwd)
        cookies = sign.login()

        # Save cookies to usercookies/<email>.json
        sign.saveCookies()
        
        
        # Response output
        ## Function for taking user prompt as input followed by producing AI generated responses
        def generate_response(prompt):
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            response = chatbot.chat(prompt)
            return response

        ## Conditional display of AI generated responses as a function of user provided prompts
        with response_container:
            with st.spinner('Generating response please wait...'):
                      time.sleep(7)
            st.success('Response generated')
            response_placeholder = st.empty()
            response_placeholder.response_container(" ")
            
            if user_input:
                 response = generate_response(user_input)
                 st.session_state.past.append(user_input)
                 words = response.split()
                 for word in words:
                     response_placeholder.response_container("Generated Result: " + " ".join(words[:words.index(word) + 1]))
                     time.sleep(0.1)
                 
                          
    if page == "Select":
        st.write("Please select the services")
    elif page == "EMI Calculator":
        loan_repay()
    elif page == "Tax Calculator":
        tax_cal()
    else:
        chatbot()
        
  
if __name__=='__main__':
    main()
    
           
