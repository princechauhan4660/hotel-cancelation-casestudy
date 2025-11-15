import streamlit as st

st.title('calculate your BMI')
height=1
weight = st.number_input('ENTER YOUR WEIGHT IN KGs :')
height = st.number_input('ENTER YOUR HEIGHT IN CMS :')
if height==0:
    bmi=0
else:
    bmi=weight/height**2

st.success(f'YOUR BMI IS : {bmi} KG/CM^2')