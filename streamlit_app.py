import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write('Hello World!')
# st.page_link('app.py', label='the best app')

st.header('I like buttons ~ meow')
st.image('https://images.hdqwalls.com/wallpapers/cute-kitten-4k-im.jpg')

if st.button('Say Meow'):
    st.write('meow')
else:
    st.write('Hello there...')


data_secs = np.arange(0, 86400, 1)
data_meow = np.random.binomial(n=1, p=np.linspace(0, 1, len(data_secs)), size=len(data_secs))
data = pd.DataFrame({'meows':data_meow,'secs':data_secs})
data = data.rolling(3600).sum()

c = alt.Chart(data).mark_line().encode(x='secs', y='meows')
st.write(c)