import streamlit as st

st.title('EDA')

cols = ['AGREEMENT_RK',
'TARGET',
'AGE',
'SOCSTATUS_WORK_FL',
'SOCSTATUS_PENS_FL',
'GENDER',
'CHILD_TOTAL',
'DEPENDANTS',
'PERSONAL_INCOME',
'LOAN_NUM_TOTAL',
'LOAN_NUM_CLOSED']

option = st.selectbox(
    'Распределение признака:',
    cols)

st.write(option)
