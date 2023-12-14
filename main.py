import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clients.csv', index_col=0)

st.title('Разведочный анализ данных о клиентах')

new_cols = {'AGREEMENT_RK' : "Идентификатор объекта",
'TARGET' : "Отклик на маркетинговую кампанию",
'AGE' : "Возраст",
'SOCSTATUS_WORK_FL' : 'Соц статус относительно работы',
'SOCSTATUS_PENS_FL' : 'Соц статус относительно пенсии',
'GENDER' : 'Пол',
'CHILD_TOTAL' : 'Кол-во детей',
'DEPENDANTS' : 'Кол-во иждивенцев',
'PERSONAL_INCOME': 'Доход клиента',
'LOAN_NUM_TOTAL': 'Кол-во ссуд',
'LOAN_NUM_CLOSED' : 'Кол-во погашенных ссуд'}

df.rename(columns=new_cols, inplace=True)

new_cols = list(new_cols.values())

st.subheader('Распределения признаков')

col = st.selectbox('Выберите признак:', new_cols[1:], key=1)

f, ax = plt.subplots()
sns.set(rc={'figure.figsize':(7,5)})
sns.set_style("whitegrid")
feature = col
sns.histplot(data=df.drop(['Идентификатор объекта'], axis=1), x=feature).set_title(f"Распределение признака {col}")
st.pyplot(f)

st.subheader('Матрица корреляций')
f, ax = plt.subplots(figsize=(15,10))
sns.heatmap(df.drop(['Идентификатор объекта'], axis=1).corr(), ax=ax, annot=True)
st.pyplot(f)
st.write('''
        Наблюдается сильная отрицательная корреляция признаков «Соц статус относительно работы» и «Соц статус относительно пенсии».
        
        Наблюдается сильная положительная корреляция между признаками «Кол-во ссуд» и «Кол-во погашенных ссуд».
        
        Не наблюдается сильной корреляции между таргетом и признаками.
        ''')



st.subheader('График попарных распределений признаков')
f1 = st.selectbox("Выберите первый признак:", new_cols[2:], key=2)
f2 = st.selectbox("Выберите второй признак:", new_cols[2:], key=3)

f = plt.figure(figsize=(7,5))
sns.scatterplot(x=df[f1], y=df[f2], data=df)
plt.title(f"Попарное распределение {f1} и {f2}")
plt.xlabel(f1)
plt.ylabel(f2)
st.pyplot(f)

st.subheader('График зависимости целевой переменной от признака')
f1 = st.selectbox("Выберите признак:", new_cols[2:], key=4)

f = plt.figure(figsize=(7,5))
sns.histplot(data=df, x=f1, hue='Отклик на маркетинговую кампанию', bins=40)
plt.xlabel('Отклик на маркетинговую кампанию')
plt.ylabel(f1)
st.pyplot(f)

st.subheader('Числовые характеристики распределения числовых столбцов')
col = st.selectbox('Выберите признак:', new_cols[1:], key=5)

descr = df[col].describe()
st.write(descr)
