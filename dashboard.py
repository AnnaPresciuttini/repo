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

# st.sidebar.title("Exploratory data analysis:")
# select = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Weekly returns',], key='1')


@st.cache
def load_data(nrows):
    data = pd.read_csv('dataset_streamlit.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(5994)
data_ = data.rename(columns={'Date':'index'}).set_index('index')

# x = st.slider('Select the year range',1999, 2020, (1999, 2020))
# st.line_chart(data_.adjclose)
cols = ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Weekly returns']
st_ms = st.multiselect("Columns", data.columns.tolist(), default=cols)


st.dataframe(data.head(500))

if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Adjusted Closing Prices':
        data_ = data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'adjclose')
#         pyplot.xlabel("Date")
#         pyplot.ylabel( 'Adjusted Closing prices')
#         pyplot.title( 'Italian adjusted closing prices history')
#         pyplot.legend().set_visible(False)
        
        

 
        

# df=pd.read_csv("dataset_streamlit.csv")
# st.dataframe(df.head())







