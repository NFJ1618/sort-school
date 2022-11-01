import streamlit as st
import time
from sorts import *
from utils import Graph, generate



st.set_page_config(layout='wide')

with st.sidebar:
    r = st.selectbox('Start array', ('Random', 'Partly Random', 'Partly Sorted', 'Almost Sorted', 'Reverse Sorted'))
    t = st.slider('Delay (ms)', 0, 1000, step=250) / 1000
    y = st.slider('Array size', 10, 100)
    sort_type = st.selectbox("Pick a sorting algorithm", ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Cycle Sort', 'Merge Sort', 'Heap Sort', "Quick Sort"))
    celebrate = st.checkbox("Celebrate!", value=False)
    # st.text("Worst case")
    # wruntime = st.latex(r[sort_type])
    # st.text("Average case")
    # aruntime = st.latex(a[sort_type])
    

x = list(generate(y, r))
correct = sorted(x)
data = Graph(correct)
data.plot(x)
placeholder = data.placeholder
title = st.header(sort_type)
subtitle = st.subheader(s[sort_type])
paragraph = st.text(p[sort_type])

with st.sidebar:
    if st.button('Start sort'):
        # text.text("Sorting")
        time.sleep(0.5)
        d[sort_type](x, data, t)
        # text.text("Sorted!")
        if celebrate:
            st.balloons()
        # if st.session_state.celebrate:
        #     st.balloons()
        #     st.session_state.celebrate = False
    
