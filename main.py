import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

st.title('Crypto Currency Tracker')

# Sidebar
st.sidebar.title('Options')
crypto_mapping = st.sidebar.selectbox('Select a crypto currency', ['BTC-USD', 'ETH-USD', 'LTC-USD', 'MSFT'])
start_date = st.sidebar.date_input('Start date', date.today() - relativedelta(months=1))
end_date = st.sidebar.date_input('End date', date.today())
st.sidebar.selectbox("Select a time period", ["1d", "5d", "1mo", "3mo", "6mo"])
selected_value = st.sidebar.selectbox("Select a value to display", ["Open", "High", "Low", "Close", "Volume"])

if st.sidebar.button('Track crypto currency'):
    crypto_hystory = yf.download(crypto_mapping, start=start_date, end=end_date)
    fig = px.line(crypto_hystory, x=crypto_hystory.index, y=selected_value, title=f'{crypto_mapping} {selected_value} price')
    st.plotly_chart(fig)
