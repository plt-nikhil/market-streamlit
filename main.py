import requests
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import json
import os
from  all_stock_data_table import get_data_for_all_stock, sector_name_count, counter_sector_chart, index_count, fetch_index_data, get_stock_name, generate_heatmap, fetch_data_from_api_stock, generate_chart



st.set_page_config(layout="wide")

df = get_data_for_all_stock()
rt = sector_name_count()
ts = counter_sector_chart()
yu = index_count()

sectors = df['sector_name'].unique().tolist()

# Add dropdown for sector filtering in col2


# sectors = df['sector_name'].unique().tolist()


d,col1, col2 = st.columns([0.20,0.30,0.30])
with d:
    selected_sector = st.selectbox('**Select Sector**', ['All'] + sectors)

# Filter data based on selected sector
    if selected_sector == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['sector_name'] == selected_sector]

with col1:
    st.write("**All Stock List**")
with col2:
    st.markdown("**Distribution of Sector Names**")

col3, col4 = st.columns([0.60,0.40])

with col3:
    st.dataframe(filtered_df)

with col4:
    
    st.plotly_chart(rt)



# Display filtered DataFrame below the main table in col3
# if selected_sector != 'All':
#     with col3:
#         st.subheader('Filtered Data')
#         st.dataframe(filtered_df)


col5,col6 = st.columns([0.2,0.1])

with col6:
        # Dropdown to select index symbol
    index_symbol = st.selectbox('Select Index Symbol', [
        "SENSEX", "BSE100", "BSE200", "BSE500", "BSE CG", "BSE CD", "BSE HC", 
        "BSEPSU", "AUTO", "METAL", "POWER", "SMEIPO", "CONDIS", "FINSER", 
        "INDSTR", "ENERGY", "TELCOM", "UTILS", "LRGCAP", "SMLSEL", "MIDSEL", 
        "SNXT50", "MID150", "SML250", "LMI250", "MSL400", "BSEPVTBANK", 
        "SERVICES", "NIFTY", "NIFTYIT", "NIFTYJR", "BANKNIFTY", "NIFTY500", 
        "MIDCAP50", "NIFTY100", "NIFTYFMCG", "NIFTYPSU", "NIFTYMNC", 
        "NIFTYSMALL", "NIFTYPSE", "NIFTYAUTO", "NIFTYMETAL", "NIFTY200", 
        "NIFTYMEDIA", "NIFTYCDTY", "NIFTYCPSE", "NIFTYPTBNK", "NCONSDUR", 
        "NOILGAS", "NIFTYMFG"
    ])

col7,col8 = st.columns([0.5,0.5])
with col7:
    st.plotly_chart(yu)

with col8:
    # st.markdown('Index Heatmap Data')



    # Fetch data based on selected index symbol
    index_data = fetch_index_data(index_symbol)

    if index_data:
        # Convert JSON data to DataFrame
        df = pd.DataFrame(index_data)

        # Display data in table format
        st.write(f"Data for {index_symbol}:")
        st.dataframe(df)


col9,non,col10 = st.columns([0.2,0.6,0.2])

with col9:
    index_symbol = st.selectbox('Select Stock Name', get_stock_name())

with col10:
    chart = st.selectbox('Select Chart',["Line","Candlestick","Bar","Area","Scatter","Histogram","Box","Violin","Pie","Sunburst","Treemap","Funnel","Polar"])

col11,col12 = st.columns([0.5,0.5])
with col11:
    index_data = generate_heatmap(index_symbol)
    st.plotly_chart(index_data)

with col12:
    data = fetch_data_from_api_stock(index_symbol)
    df = pd.DataFrame(data)
    figure = generate_chart(df, chart)
    st.plotly_chart(figure)

col13,col14 = st.columns([0.9,0.1])
with col13:
    st.write("**Comming Soon gainer & Ipo & Mover Stock @ Maulik Patel**")