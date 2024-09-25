import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
data=pd.read_csv('wholesale.csv')
st.write(data)

value=data['Region'].unique()
display1=['Delhi','Banglore','Chennai']
op1=st.sidebar.selectbox("Choose product",(value),format_func=lambda x:display1[x-1])

value1=data['Channel'].unique()
display=['Hotel','Retail']
op2=st.sidebar.selectbox('Select a channel',(value1),format_func=lambda x:display[x-1])

col1,col2,col3=st.columns(3)

df=data[data['Region']==op1]
df1=df[df['Channel']==op2]

col1.metric('Total Fresh',df1['Fresh'].sum())

col2.metric('Total Milk',df1['Milk'].sum())

col3.metric('Grocery items',df1['Grocery'].sum())

col4,col5,col6=st.columns(3)

col4.metric('Frozen items',df1['Frozen'].sum())

col5.metric('Total Papers',df1['Detergents_Paper'].sum())

col6.metric('Total Delicassen',df1['Delicassen'].sum())

st.write(df1)

st.header('Bar Chart')
chart={'Fresh':df1['Fresh'].sum(),
        'Milk':df1['Milk'].sum(),
        'Grocery_items':df1['Grocery'].sum(),
        'Frozen items':df1['Frozen'].sum(),
        'Total Papers':df1['Detergents_Paper'].sum(),
        'Total Delicassen':df1['Delicassen'].sum()
        }

st.bar_chart(chart)

st.header('Pie Chart')
fig = px.pie(values=list(chart.values()),
             names=list(chart.keys()))
st.plotly_chart(fig)



