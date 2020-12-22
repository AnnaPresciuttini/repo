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

st.sidebar.title("Select one of the feature to see the time series:")
select = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns',], key='1')
st.sidebar.title("Select one of the feature to see the boxplot:")
select_2 = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns',], key='2')


@st.cache
def load_data(nrows):
    data = pd.read_csv('dataset_streamlit.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(5994)
st.dataframe(data.head(500))

if st.checkbox("Show dataset with selected columns"):
        # get the list of columns
        columns = data.columns.tolist()
        st.write("#### Which columns do you want to see?")
        selected_cols = st.multiselect("", columns)
        selected_data = data[selected_cols]
        st.dataframe(selected_data)
        
if st.checkbox("Show number of rows"):
        st.write('5994')
if st.checkbox("Show number of columns"):
        st.write('9')

# Show dataset description
if st.checkbox("Show description of dataset"):
        st.write(data.describe())
        
if st.checkbox("Show correlations"):
            st.write("### Heatmap")
            fig, ax = plt.subplots(figsize=(10,10))
            st.write(sns.heatmap(data[['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns']].corr(2), annot=True,linewidths=0.5))
            st.pyplot()


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


#     if select_2 == 'High':
#          st.write(seaborn.boxplot(data.high)
#     if select_2 == 'Low':
#          st.write(seaborn.boxplot(data.low)
#     if select_2 == 'Close':
#          st.write(seaborn.boxplot(data.close)
#     if select_2 == 'Volume':
#          st.write(seaborn.boxplot(data.volume)
#     if select_2 == 'Weekly returns':
#          st.write(seaborn.boxplot(data.weekly_returns)
    
    
    
        

 
        








