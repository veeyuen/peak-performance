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


#categories = ['Activity', 'Strength', 'Stamina', 'Sleep', 'Stress<br>Management', 'Mental Health', 'Cognitive Function', 'Sick Leaves', 'Energy Levels']
#categories = [*categories, categories[0]]

#Day_0 = [1.9, 4, 3, 3, 3, 5.5, 3.5, 1, 3]
#Day_30 = [4.15, 6, 5, 10, 7, 6.9, 5.5, 8.8, 5]
#Day_60 = [7.8, 9, 8, 10, 10, 8.06, 8, 10, 8]
#Day_0 = [*Day_0, Day_0[0]]
#Day_30 = [*Day_30, Day_30[0]]
#Day_60 = [*Day_60, Day_60[0]]

#fig = go.Figure(
#    data=[
#        go.Scatterpolar(r=Day_60, theta=categories, fill='toself', name='Day 60'),
#        go.Scatterpolar(r=Day_30, theta=categories, fill='toself', name='Day 30'),
#        go.Scatterpolar(r=Day_0, theta=categories, fill='toself', name='Day 0')
#    ],
#    layout=go.Layout(
#        title=go.layout.Title(text='Peak Performance - XXXX'),
#        polar={'radialaxis': {'visible': True}},
#        showlegend=True
#    )
#)

#polar=dict(
#    radialaxis=dict(
#      visible=True,
#      range=[1, 10]
#    )),
#      showlegend=True
    
#)
#fig.update_layout(template="plotly_dark", title="Peak Performance")

#if __name__ == '__main__':
#pyo.plot(fig)

#st.plotly_chart(fig)

random_x = np.array([0, 30, 60, 90])
recovery_y0 = np.array([np.nan, np.nan, 10.66, 12.88])
nutrition_y1 = np.array([np.nan, np.nan, 12.53, 16.47])
exercise_y2 = np.array([np.nan, np.nan, 15.47, 21.51])
overall_y3 = np.array([np.nan, np.nan, 12.00, 15.32])

x_peak = [0, 30, 60]
y_0 = [1.9, 4, 3, 3, 3, 5.5, 3.5, 1, 3]
y_30 = [4.15, 6, 5, 10, 7, 6.9, 5.5, 8.8, 5]
y_60 = [7.8, 9, 8, 10, 10, 8.06, 8, 10, 8]

r1 =[1.9, 4, 3, 3, 3, 5.5, 3.5, 1, 3]

fig = make_subplots(
    rows=3, cols=2,
    specs=[[{"type": "polar", "rowspan":2, "colspan":2}],
           [{"type": "scatter"}, {"type": "scatter"}],
           [{"type": "scatter"}, {"type": "scatter", "rowspan": 2}]
              ],
    horizontal_spacing= 0.20, vertical_spacing= 0.15,
    row_heights=[0.7, 0.4, 0.4]
    )

fig.add_trace(
    go.Scatterpolar(
        theta=['Activity', 'Strength', 'Stamina', 'Sleep', 'Stress<br>Management', 'Mental Health', 'Cognitive Function', 'Sick Leaves', 'Energy Levels'],
        r=y_0,
        fill='toself',
        name='Day 0',
        legend="legend1"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatterpolar(
        theta=['Activity', 'Strength', 'Stamina', 'Sleep', 'Stress<br>Management', 'Mental Health', 'Cognitive Function', 'Sick Leaves', 'Energy Levels'],
        r=y_30,
        fill='toself',
        name='Day 30',
        legend="legend1"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatterpolar(
        theta=['Activity', 'Strength', 'Stamina', 'Sleep', 'Stress<br>Management', 'Mental Health', 'Cognitive Function', 'Sick Leaves', 'Energy Levels'],
        r=y_60,
        fill='toself',
        name='Day 60',
        legend="legend1"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatter(
        x=x_peak, y=recovery_y0,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=2,
    col=1,

    )

fig.add_trace(
    go.Scatter(
        x=x_peak, y=nutrition_y1,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=2,
    col=2,
    )

fig.add_trace(
    go.Scatter(
        x=x_peak, y=exercise_y2,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=3,
    col=1,
    )

fig.add_trace(
    go.Scatter(
        x=x_peak, y=overall_y3,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='royalblue', width=2),
        showlegend=False
    ),
    row=3,
    col=2,
    )



fig.update_layout(
    autosize=False,
#    minreducedwidth=350,
#    minreducedheight=350,
    width=1150,
    height=1500,
#    title_text = 'PEAK PERFORMANCE',

    font=dict(
        family="Courier New, monospace",
        size=12,  # Set the font size here
        color="White"
    ),

    title_xref="paper",

    margin=dict(l=10, r=78),


    title={
        'text': "Peak Performance",
        'y':0.9,
        'x':0.2,
        'xanchor': 'center',
        'yanchor': 'top'},

    title_font_family="Times New Roman",
    title_font_color="black",

    polar=dict(            # first chart y-axis labels
    radialaxis=dict(
      visible=True,
      range=[1, 10],
        tickfont_size = 12,
        color="Yellow"
    )),

    polar2=dict(        # second chart y-axis labels
    radialaxis=dict(
      visible=True,
      range=[0, 10],
        tickfont_size = 12,
        color="Yellow"
    )),


    template="plotly_dark",

    legend1=dict(
        title= "RECOVERY",
        x=-0.05,
        y=1.1,
        title_font_family="Arial",
        font=dict(
            family="Arial",
            size=10,
            color="White"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=1
    )




#fig.update_polars(
#    radialaxis=dict(
##        angle=45
#    )
#)

fig.update_xaxes(title_text="Days", row=2, col=1)
fig.update_yaxes(title_text="Recovery<br>Activity", row=2, col=1)
fig.update_xaxes(title_text="Days", row=2, col=2)
fig.update_yaxes(title_text="Nutrition<br>Activity", row=2, col=2)
fig.update_xaxes(title_text="Days", row=3, col=1)
fig.update_yaxes(title_text="Exercise<br>Activity", row=3, col=1)
fig.update_xaxes(title_text="Days", row=3, col=2)
fig.update_yaxes(title_text="Overall<br>Performance", row=3, col=2)


st.plotly_chart(fig)

