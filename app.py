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


np.random.seed(1)

N = 10
random_x = np.linspace(0, 300, N)
random_y0 = np.random.randn(N)
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)
random_y3 = np.random.randn(N)

x_recovery = np.array([0, 30, 60, 90])
y_recovery = np.array([3.64, 8.47, 9.52, 9.59])

x_nutrition = np.array([0, 30, 60, 90])
y_nutrition = np.array([2.12, 7.02, 9.00, 9.875])

x_training = np.array([0, 30, 60, 90])
y_training = np.array([2.96, 5.05, 8.26, 9.67])

x_overall = np.array([0, 30, 60, 90])
y_overall = np.array([3.2, 7.5, 9.16, 9.66])


N = 10
t = np.linspace(0, 1, N)
freq = 1.0

c = np.sin(2 * np.pi * freq * t + 0.0)
d = np.sin(2 * np.pi * -0.23 * t + 0.0)
e = np.sin(2 * np.pi * 0.25 * t + 0.0)
f = np.sin(2 * np.pi * 0.9 * t + 0.0)



x_sinwave=t*300
y_sinwave=c


r1 =[3,3,5.5]

fig = make_subplots(
    rows=4, cols=2,
    specs=[[{"type": "polar"}, {"type": "polar"}],
           [{"type": "scatter"}, {"type": "scatter"}],
           [{"type": "polar"}, {"type": "scatter", "rowspan": 2}],
           [{"type": "scatter"}, None]
              ],
    horizontal_spacing= 0.20, vertical_spacing= 0.15,
    row_heights=[0.7, 0.3, 0.7, 0.3]
    )



fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Sleep<br>Quality<b>", "<b>Stress<br>Management<b>", "<b>Mental<br>Health<b>"],
        r=[7.8,9,8],
        fill='toself',
        name='Day 60',
        legend="legend1"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Sleep<br>Quality<b>", "<b>Stress<br>Management<b>", "<b>Mental<br>Health<b>"],
        r=[10,7,6.9],
        fill='toself',
        name='Day 30',
        legend="legend1"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Sleep<br>Quality<b>", "<b>Stress<br>Management<b>", "<b>Mental<br>Health<b>"],
        r=r1,
        fill='toself',
        name='Day 0',
        legend="legend1"
    ),
    row=1,
    col=1,
)





fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Cognitive<br>Function<b>", "<b>Sick<br>Leaves<b>", "<b>Energy<br>Levels<b>"],
        r=[8,10,8],
        fill='toself',
        name='Day 60',
        legend="legend2"
    ),
    row=1,
    col=2,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Cognitive<br>Function<b>", "<b>Sick<br>Leaves<b>", "<b>Energy<br>Levels<b>"],
        r=[5.5,8.8,5],
        fill='toself',
        name='Day 30',
        legend="legend2"
    ),
    row=1,
    col=2,
)


fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Cognitive<br>Function<b>", "<b>Sick<br>Leaves<b>", "<b>Energy<br>Levels<b>"],
        r=[3.5,1,3],
        fill='toself',
        name='Day 0',
        legend="legend2"
    ),
    row=1,
    col=2,
)


fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Level<b>", "<b>Stamina<b>"],
        r=[7.8,9,8],
        fill='toself',
        name='Day 60',
        legend="legend3"
    ),
    row=3,
    col=1,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Level<b>", "<b>Stamina<b>"],
        r=[4.15,6,5],
        fill='toself',
        name='Day 30',
        legend="legend3"
    ),
    row=3,
    col=1,
)


fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Level<b>", "<b>Stamina<b>"],
        r=[1.9,4.4,3],
        fill='toself',
        name='Day 0',
        legend="legend3"
    ),
    row=3,
    col=1,
)



fig.add_trace(
    go.Scatter(
        x=x_recovery, y=y_recovery,
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
        x=x_nutrition, y=y_nutrition,
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
        x=x_training, y=y_training,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=4,
    col=1,
    )

fig.add_trace(
    go.Scatter(
        x=x_overall, y=y_overall,
        mode='lines',
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
      range=[0, 10],
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
    ),

    legend2=dict(
        title="NUTRITION",
        x=0.55,
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
    ),

    legend3=dict(
        title="TRAINING",
        x=-0.05,
        y=0.5,
        title_font_family="Arial",
        font=dict(
            family="Arial",
            size=10,
            color="White"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=1
    ),

  showlegend=True
)

fig.update_polars(
    radialaxis=dict(
        angle=45,
        range=[1, 10]
    )
)

#fig.update_polars(radialaxis=dict(range=[0, 1]))

fig.update_xaxes(title_text="Days", row=2, col=1)
fig.update_yaxes(title_text="Recovery<br>Activity", row=2, col=1)
fig.update_xaxes(title_text="Days", row=2, col=2)
fig.update_yaxes(title_text="Nutrition<br>Activity", row=2, col=2)
fig.update_xaxes(title_text="Days", row=4, col=1)
fig.update_yaxes(title_text="Training<br>Activity", row=4, col=1)
fig.update_xaxes(title_text="Days", row=3, col=2)
fig.update_yaxes(title_text="Overall<br>Performance", row=3, col=2)




# use below only if necessary
#fig.update_traces(mode = "lines+markers",
#      r = [1,2,3,4,5],
#      theta = [0,90,180,360,0],
#      line_color = "magenta",
#      marker = dict(
#        color = "royalblue",
#        symbol = "square",
#        size = 8
#      ))



st.plotly_chart(fig)
