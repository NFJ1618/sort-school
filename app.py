import streamlit as st
import time
from sort_school.sorts import *
from sort_school.utils import Graph, generate



st.set_page_config(layout='wide')

with st.sidebar:
    link='[Sort School by NFJ1618](https://nfj1618.github.io/)'
    st.title(link)
    r = st.selectbox('Start array', ('Random', 'Partly Random', 'Partly Sorted', 'Almost Sorted', 'Reverse Sorted'))
    t = st.slider('Delay (ms)', 0, 1000, step=250) / 1000
    y = st.slider('Array size', 10, 100)
    sort_type = st.selectbox("Pick a sorting algorithm", ('Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Cycle Sort', 'Merge Sort', 'Heap Sort', "Quick Sort"))
    celebrate = st.checkbox("Celebrate!", value=False)
    # st.text("Worst case")
    # wruntime = st.latex(r[sort_type])
    # st.text("Average case")
    # aruntime = st.latex(a[sort_type])
    

title = st.header(sort_type + " - " + s[sort_type])
#subtitle = st.markdown()
x = list(generate(y, r))
correct = sorted(x)
data = Graph(correct, sort_type=="Merge Sort")
data.plot(x, x)
placeholder = data.placeholder
paragraph = st.markdown(p[sort_type])

with st.expander('Code (Python3)', expanded=False):
    st.code(code[sort_type])


with st.expander("Time Complexities", expanded=True):
    col0, col1, col2, col3, col4, col5, col6, col7 = st.columns(8)

    with col0:
        st.markdown("Sort")
        st.text("")
        st.markdown("Average case")
        st.text("")
        st.markdown("Worst case")


    for sort, col in zip(sorted(d.keys()) ,(col1, col2, col3, col4, col5, col6, col7)):
        with col:
            st.markdown(sort)
            st.latex(average[sort])
            st.latex(worst[sort])

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
    
