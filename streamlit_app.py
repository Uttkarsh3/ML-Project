import streamlit as st
import pandas as pd

st.title('📌 Smart Home Energy Management System')

st.info('An end-to-end pipeline using Energy data for prediction electricity demand!')

df = pd.read_csv('https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set/data', sep=';',
                  parse_dates={'dt' : ['Date', 'Time']}, dayfirst=True, 
                 low_memory=False, na_values=['nan','?'],index_col='dt')
df
