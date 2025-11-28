import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chart_studio.plotly as py

import plotly.graph_objs as go

import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode , plot , iplot

df = pd.read_csv(r'C:/Users/JAYSHREE/Desktop/python project analyst/bitcoin_price_Training - Training.csv')
df['Date']= df['Date'].astype('datetime64[ns]')
df.sort_values(by = "Date")
data = df.sort_index(ascending=False).reset_index()
data.drop('index' , axis = 1, inplace = True)
bitcoin_sample = data[0:100]




st.set_page_config(page_title="Bitcoin Dashboard",
                   layout="wide")

st.title("Comprehensive Bitcoi Price Analysis Dashboard")

## 1st plot:
st.subheader("Bitcoin Candlestick Chart (First 100 Days)")
trace = go.Candlestick(x=bitcoin_sample['Date'],
              high = bitcoin_sample['High'],
              open = bitcoin_sample['Open'],
              close = bitcoin_sample['Close'],
              low = bitcoin_sample['Low'])

candle_data = [trace]
layout = {
    'title': 'Bitcoin Historical Prices',
    'xaxis':{'title':'Date'}
}
fig_candle = go.Figure(data = candle_data, layout=layout)
fig_candle.update_layout(xaxis_rangeslider_visible = False)
st.plotly_chart(fig_candle, use_container_width= True)

