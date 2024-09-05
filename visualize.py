import streamlit as st
import pandas as pd

def app():
    st.header(':blue[Visualization] :red[of Weather model]')
    st.write(':red[Here in this section we present the EDA we perform to visualize the dataset.]')
    dataset = pd.read_csv('forecast_data.csv')
    st.dataframe(dataset , )
    st.image('CorrelationHeatMap.jpg' , 'Heat Map')
    st.image('pairplot.jpeg' , 'All the variables pairplot')
    st.image('hist.jpeg' , 'Histogram')