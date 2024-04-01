import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import random
from plotly.subplots import make_subplots

from pathlib import Path
from PIL import Image

import numpy as np
import math

#images_folder = '/Users/veesheenyuen/Desktop/DataScience/Peak/'
#image_path = images_folder/peak-logo.png

#main_image = Image.open('/Users/veesheenyuen/Desktop/peak-logo.png')
#st.image (main_image, caption='TEST') 

categories = ['Activity', 'Strength', 'Stamina', 'Sleep', 'Stress<br>Management', 'Mental Health', 'Cognitive Function', 'Sick Leaves', 'Energy Levels']
categories = [*categories, categories[0]]

Day_0 = [1.9, 4, 3, 3, 3, 5.5, 3.5, 1, 3]
Day_30 = [4.15, 6, 5, 10, 7, 6.9, 5.5, 8.8, 5]
Day_60 = [7.8, 9, 8, 10, 10, 8.06, 8, 10, 8]
Day_0 = [*Day_0, Day_0[0]]
Day_30 = [*Day_30, Day_30[0]]
Day_60 = [*Day_60, Day_60[0]]

fig = go.Figure(
    data=[
        go.Scatterpolar(r=Day_60, theta=categories, fill='toself', name='Day 60'),
        go.Scatterpolar(r=Day_30, theta=categories, fill='toself', name='Day 30'),
        go.Scatterpolar(r=Day_0, theta=categories, fill='toself', name='Day 0')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Peak Performance - XXXX'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

polar=dict(
    radialaxis=dict(
      visible=True,
      range=[1, 10]
    )),

  showlegend=True
)
fig.update_layout(template="plotly_dark", title="Peak Performance")

#if __name__ == '__main__':
#pyo.plot(fig)

st.plotly_chart(fig)



