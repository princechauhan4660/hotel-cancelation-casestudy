import numpy as np
import pandas as pd 
import streamlit as st
import joblib


# lets loasd all the instances required over here 
with open('transformer.joblib','rb') as file:
    transformer = joblib.load(file)

# lest load the model
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)

st.title('INN HOTEL GROUP')
st.header(':blue[THS APPLICATION WILL PREDICT THE CHANCES OF BOOKING  CANCELATION]')


# lets see how prediction will happe
amnth = st.slider('SELECT YOUR MONTH OF ARRIVAL ',min_value=1,max_value=12)
wkd_lambda = (lambda x:0 if x=='Monday' else
              1 if x=='Tuesday' else
              2 if x=='Wednesday' else
              3 if x=='Thursday' else
              4 if x=='Friday' else
              5 if x=='Saturday' else 6)

awkd = st.selectbox('SELCT YOIR WEEK DAY OF ARRIVAL',['Mondnay','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
dwkd = wkd_lambda(st.selectbox('SELECT YOUR wEEKDAY OF DEPARTURE ',['Mondnay','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']))

wkend = st.number_input('ENTER HOW MANY WEEKEND NIGHT ARE THEIR IN STAY',min_value=0)

wk = st.number_input('ENTER HOW MANY WEEK NIGHTS ARE THAIR IN STAY ',min_value=0)

totan = wkend+wk
mkt = (lambda x:0 if x=='offline' else 1)(st.selectbox('HOW BOOKING HAS BEEN MADE ',['OFLINE','ONLINE']))

lt = st.number_input(' HOW MANY DAYS PRIOR THE BOOKING HAS BEEN MADE ',min_value=0)
price = st.number_input('WHAT IS THE averrage price per room ',min_value=0)
adults = st.number_input('HOW AMNY ADULTS MEMBERS IN THE BOOKING ',min_value=0)
spcl = st.selectbox(' SELECT THE NUMBER OF THE SPECIAL REQUESTS MADE ',[0,1,2,3,4,5])

park = (lambda x: 0 if x== 'NO' else 1)(st.selectbox('DOES GUEST REQUEST FOR PARKIG SPACE',['YES','NO']))


# LETS TRANFORM THE DATA 

lt_t,price_t = tranfromer.transform([[lt,price]])[0]

# create input list 
input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth.totan,dwkd]

# mke prediction 

prediction = model.predict_proba[input_list][:,1][0]

# lets show thw probability 

if st.button('probability'):
    st.success(f'CANCELATION CHANCES {round(prediction,4)*100}')
