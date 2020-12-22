# -*- coding: utf-8 -*-
"""dashboard

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17XZr1EnkoFxb6Kne29VQMMtlqBp8EtG7
"""

# !pip install ipykernel
# !pip install -q streamlit

# import streamlit as st

# exit()

import streamlit as st
import plotly.express as px 

# Commented out IPython magic to ensure Python compatibility.
import numpy as np 

# data processing
import pandas as pd 
# data visualization
# import seaborn as sns
# %matplotlib inline
# from matplotlib import pyplot as plt
# from matplotlib import style

st.title('Predicting weekly returns of the FTSE MIB Index')

st.sidebar.title("Exploratory data analysis:")
select = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns',], key='1')


@st.cache
def load_data(nrows):
    data = pd.read_csv('dataset_streamlit.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(5994)
st.dataframe(data.head(500))

data_ = data.rename(columns={'Date':'index'}).set_index('index')

# x = st.slider('Select the year range',1999, 2020, (1999, 2020))
# st.line_chart(data_.adjclose)





if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Adjusted Closing Prices':
        st.line_chart(data_.adjclose)
    if select == 'Open':
        st.line_chart(data_.open)
    if select == 'High':
        st.line_chart(data_.high)
    if select == 'Low':
        st.line_chart(data_.low)
    if select == 'Close':
        st.line_chart(data_.close)
    if select == 'Volume':
        st.line_chart(data_.volume)
    if select == 'Weekly returns':
        st.line_chart(data_.weekly_returns)
    
    
    
        

 
        

# df=pd.read_csv("dataset_streamlit.csv")







