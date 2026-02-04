import streamlit as st
from functions.plot import plot_ts

st.title('Stocks History')
st.write('Look the stocks values.')

ticker = st.sidebar.text_input(
    'Choose the ticker:', value = 'AAPL'
)

fig =plot_ts(ticker)

st.plotly_chart(fig)