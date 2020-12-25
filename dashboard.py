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
import datetime
st.set_option('deprecation.showPyplotGlobalUse', False)

import plotly.express as px

# import pickle
# pickle_in = open('classifier.pkl', 'rb') 
# classifier = pickle.load(pickle_in) 

from scipy.stats import norm  
import plotly.figure_factory as ff
z = [[1, 1, 1, 1, -0.39,1, 0.02],
     [1, 1, 1, 1, -0.4,1, 0.03],
     [1, 1, 1, 1, -0.4,1, 0.02],
     [1, 1, 1, 1, -0.4,1, 0.03],
     [-0.39, -0.4, -0.4, -0.4, 1,-0.4, -0.09],
     [1, 1, 1, 1, -0.4,1, 0.03],
     [0.02, 0.03, 0.02, 0.03, -0.09, 0.03,1]]

x = ['high', 'low', 'open', 'close', 'volume', 'adjclose', 'weekly_returns']
y = ['high', 'low', 'open', 'close', 'volume', 'adjclose', 'weekly_returns']
# fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z, colorscale='Viridis')
# fig.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np 

# data processing
import pandas as pd 
# data visualization
# import seaborn as sns
# %matplotlib inline
from matplotlib import pyplot as plt
# from matplotlib import style

st.title('Predicting weekly returns of the FTSE MIB Index')
st.markdown("Welcome!")

st.sidebar.title("Select one of the feature to see the time series:")
select = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns',], key='1')
st.sidebar.title("Select one of the feature to see the boxplot:")
select_2 = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High','Volume', 'Low', 'Close', 'Weekly returns',], key='2')
st.sidebar.title("Select a feature to see an interactive histogram:")
select_3 = st.sidebar.selectbox('Feature', ['Adjusted Closing Prices', 'Open', 'High', 'Low', 'Close', 'Weekly returns'], key='3')

@st.cache
def load_data(nrows):
    data = pd.read_csv('dataset_streamlit_app.csv', nrows=nrows)
    return data


data_load_state = st.text('Loading data...')
data = load_data(5544)
st.dataframe(data.head(500))

if st.checkbox("Do you want to visualize only some columns?"):
        # get the list of columns
        columns = data.columns.tolist()
        st.write("#### Which columns do you want to see?")
        selected_cols = st.multiselect("", columns)
        selected_data = data[selected_cols]
        st.dataframe(selected_data)
        
if st.checkbox("Show number of rows"):
        st.write('5593')
if st.checkbox("Show number of columns"):
        st.write('8')

# Show dataset description
if st.checkbox("Show summary statistics"):
        st.write(data.describe())
        
if st.checkbox("Show correlations heatmap"):
            st.write("### Heatmap")
            st.write(ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z, colorscale='Viridis'))

if st.checkbox("Show distribution of the features"):
            st.write("### Histograms")
            data[['high', 'low', 'open', 'close', 'volume', 'adjclose', 'weekly_returns']].hist(bins=15, figsize=(15, 6), layout=(2, 4), color='lightblue', grid=False)
            plt.show()
            st.pyplot()
 
if st.checkbox("Are weekly returns normally distributed?"):
            st.write("### Let's see...")
            fig = plt.figure()
            ax = fig.add_subplot(222)
            ax.set_xlim([-0.3, 0.2])
            data['weekly_returns'].hist(ax= ax,bins=190, color='cadetblue')
            ax1 = ax.twinx()
#             plt.title("Weekly returns distribution")
            data['weekly_returns'].plot(kind="kde", color='steelblue', ax=ax1, legend=False )
            plt.show()
            st.pyplot()
            
if st.checkbox("Do you want to overlay a normal distribution on the histogram?"):
            data['weekly_returns'].hist(bins=280, color='cadetblue', density=True)
            plt.xlim(-0.3, 0.2)
            plt.plot( np.arange(-0.2, 0.2, 0.001), norm.pdf( np.arange(-0.2, 0.2, 0.001), 0.00013255652939758521,0.033349675649634244), label = "Normal distribution")
            plt.title("Actual distribution of weekly stock returns vs normal distribution")
            plt.legend() 
            plt.show()
            st.pyplot()
            st.write("### ... they are not normally distributed")


# data_ = data.rename(columns={'Date':'index'}).set_index('index')

# x = st.slider('Select the year range',1999, 2020, (1999, 2020))
# st.line_chart(data_.adjclose)





if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Adjusted Closing Prices':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'adjclose')
        plt.xlabel("Date")
        plt.ylabel( 'Adjusted Closing prices')
        plt.title( 'Italian adjusted closing prices history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()       
    if select == 'Open':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'open')
        plt.xlabel("Date")
        plt.ylabel( 'Opening prices')
        plt.title( 'Italian opening prices history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()
    if select == 'High':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'high')
        plt.xlabel("Date")
        plt.ylabel( 'Highest prices')
        plt.title( 'Italian highest prices history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()
    if select == 'Low':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'low')
        plt.xlabel("Date")
        plt.ylabel( 'Lowest prices')
        plt.title( 'Italian lowest prices history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()
    if select == 'Close':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'close')
        plt.xlabel("Date")
        plt.ylabel( 'Closing prices')
        plt.title( 'Italian closing prices history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()
    if select == 'Volume':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'volume')
        plt.xlabel("Date")
        plt.ylabel( 'Volumes')
        plt.title( 'Historical Daily Transactions Volume')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()
    if select == 'Weekly returns':
        data_= data.loc[data['Date'] >= '1999-1-01']
        data_.plot(x='Date', y= 'high')
        plt.xlabel("Date")
        plt.ylabel( 'Weekly returns')
        plt.title( 'Weekly returns history')
        plt.legend().set_visible(False)
        plt.show()
        st.pyplot()   


    if select_2 == 'High':
         st.write( px.box(data, y="high"))
    if select_2 == 'Volume':
         st.write( px.box(data, y="volume"))
    if select_2 == 'Close':
         st.write( px.box(data, y="close"))
    if select_2 == 'Open':
         st.write( px.box(data, y="open"))
    if select_2 == 'Weekly returns':
         st.write( px.box(data, y="weekly_returns"))
    if select_2 == 'Adjusted Closing Prices':
         st.write( px.box(data, y="adjclose"))
    if select_2 == 'Low':
         st.write( px.box(data, y="low"))
    
    
    if select_3 == 'High':
        values = st.sidebar.slider("High price range", float(data.high.min()), 50000., (0., 3000.))
        f = px.histogram(data.query(f"high.between{values}"), x="high", nbins=18, title="High distribution")
        f.update_xaxes(title="High")
        f.update_yaxes(title="Values")
        st.plotly_chart(f)
    
        
    if select_3 == 'Close':
        values_3 = st.sidebar.slider("Close range", float(data.close.min()), 50000., (0., 3000.))
        f_3 = px.histogram(data.query(f"close.between{values_3}"), x="close", nbins=18, title="Close distribution")
        f_3.update_xaxes(title="Close")
        f_3.update_yaxes(title="Values")
        st.plotly_chart(f_3)
        
    if select_3 == 'Open':
        values_4 = st.sidebar.slider("Open range", float(data.open.min()), 50000., (0., 3000.))
        f_4 = px.histogram(data.query(f"open.between{values_4}"), x="open", nbins=18, title="Open distribution")
        f_4.update_xaxes(title="Open")
        f_4.update_yaxes(title="Values")
        st.plotly_chart(f_4)
        
    if select_3 == 'Weekly returns':
        values_5 = st.sidebar.slider("Weekly returns range", float(data.weekly_returns.min()), 0.3, (0., 0.))
        f_5 = px.histogram(data.query(f"weekly_returns.between{values_5}"), x="weekly_returns", nbins=18, title="Weekly returns distribution")
        f_5.update_xaxes(title="Weekly returns")
        f_5.update_yaxes(title="Values")
        st.plotly_chart(f_5)
        
    if select_3 == 'Adjusted Closing Prices':
        values_6 = st.sidebar.slider("Adj close range", float(data.adjclose.min()), 50000., (0., 3000.))
        f_6 = px.histogram(data.query(f"adjclose.between{values_6}"), x="adjclose", nbins=18, title="Adjclose distribution")
        f_6.update_xaxes(title="Adj Close")
        f_6.update_yaxes(title="Values")
        st.plotly_chart(f_6)
        
    if select_3 == 'Low':
        values_7 = st.sidebar.slider("Low range", float(data.low.min()), 50000., (0., 3000.))
        f_7 = px.histogram(data.query(f"low.between{values_7}"), x="low", nbins=18, title="Low distribution")
        f_7.update_xaxes(title="Low")
        f_7.update_yaxes(title="Values")
        st.plotly_chart(f_7)
    

 
        








