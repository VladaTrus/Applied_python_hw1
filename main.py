import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clients.csv')

st.title('Разведочный анализ данных о клиентах')

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

f, ax = plt.subplots()
sns.set(rc={'figure.figsize':(7,5)})
sns.set_style("whitegrid")
feature = option
sns.histplot(data=df, x=feature).set_title(f"Распределение признака {option}")
st.pyplot(f)
