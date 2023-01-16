#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:13:30 2023

@author: fp.b
"""

import streamlit as st
import yfinance as yf
import pandas as pd


st.title('Interactive Finance Dashboard for Data Analytics Portfolio-Francesco Paolo Bellifemina')

tickers = ('BTC-USD', 'ETH-USD', 'SOL-USD', 'AVAX-USD', 'ALGO-USD', 'UNI7083-USD')

dropdown = st.multiselect('Choose your crypto', 
                          tickers)

start = st.date_input('Start', value= pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
    

