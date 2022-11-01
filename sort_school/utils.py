import plotly.express as px
import streamlit as st
import pandas as pd
from random import randint, shuffle
from math import sqrt

def pseudo_shuffle(t, n, times, close=None):
    for i in range(times):
        if close is None:
            begin, end = randint(0, n-1), randint(0,n-1)
        else:
            begin = randint(0, n-1)
            end = randint(max(0, begin-close),min(n-1, begin+close))
        t[begin],t[end] = t[end], t[begin]

@st.cache
def generate(n, shuf_type):
    t = [i for i in range(1, n+1)]
    if shuf_type == "Random":
        shuffle(t)
    elif shuf_type == "Partly Random":
        pseudo_shuffle(t, n, n, n//2)
    elif shuf_type == "Partly Sorted":
        pseudo_shuffle(t, n, n, int(sqrt(n)))
    elif shuf_type == "Almost Sorted":
        pseudo_shuffle(t, n, n, 1)
    elif shuf_type == "Reverse Sorted":
        t = sorted(t, reverse=True)
    return t

class Graph:
    def __init__(self, correct):
        self.correct = correct
        self.placeholder = st.empty()

    def graph(self, x):
        df = pd.DataFrame({"array": x, "sorted": ['True' if x[i] == self.correct[i] else 'False' for i in range(len(x))]})

        data = px.bar(
            df,
            y="array",
            color="sorted",
            color_discrete_map={
                "True": "rgb(14, 146, 194)",
                "False": "rgb(217, 17, 74)"
            }
            
            )
        data.update_traces(hoverinfo='none', hovertemplate=None)
        data.update_layout(
            showlegend=False, 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            )
        data.update_xaxes(visible=False)
        data.update_yaxes(visible=False)
        return data

    def plot(self, x):
        self.placeholder.plotly_chart(self.graph(x), use_container_width=True)