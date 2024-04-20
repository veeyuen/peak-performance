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



r1 =[3,3,5.5]

fig = make_subplots(
    rows=1, cols=3,
    specs=[
        [{"type": "polar"}, {"type": "polar"}, {"type": "polar"}]
          ],
    horizontal_spacing= 0.20, vertical_spacing= 0.15,
    row_heights=[0.9]
    )

#fig = make_subplots(
#    rows=2, cols=2,
#    specs=[[{"type": "polar"}, {"type": "polar"}],
#           [{"type": "polar"}, None]
#              ],
#    horizontal_spacing= 0.20, vertical_spacing= 0.15,
#    row_heights=[0.7, 0.7]
#    )



fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Sleep<br>Quality<b>", "<b>Stress<br>Management<b>", "<b>Mental<br>Health<b>"],
        r=[10,10,8.06],
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
    row=1,
    col=3,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Level<b>", "<b>Stamina<b>"],
        r=[4.15,6,5],
        fill='toself',
        name='Day 30',
        legend="legend3"
    ),
    row=1,
    col=3,
)


fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Level<b>", "<b>Stamina<b>"],
        r=[1.9,4,3],
        fill='toself',
        name='Day 0',
        legend="legend3"
    ),
    row=1,
    col=3,
)





fig.update_layout(
    autosize=False,
#    minreducedwidth=350,
#    minreducedheight=350,
    width=950,
    height=650,
#    title_text = 'PEAK PERFORMANCE',

    font=dict(
        family="Courier New, monospace",
        size=9,  # Set the font size here
        color="White"
    ),

    title_xref="paper",

    margin=dict(l=10, r=78, t=5, b=5),


    #title={
    #    'text': "Peak Performance",
    #    'y':0.9,
    #    'x':0.2,
    #    'xanchor': 'center',
    #    'yanchor': 'top'},

    title_font_family="Times New Roman",
    title_font_color="black",

    polar=dict(            # first chart y-axis labels
    radialaxis=dict(
      visible=True,
      range=[0, 10],
        tickfont_size = 9,
        color="Yellow"
    )),

    polar2=dict(        # second chart y-axis labels
    radialaxis=dict(
      visible=True,
      range=[0, 10],
        tickfont_size = 9,
        color="Yellow"
    )),


    template="plotly_dark",

    legend1=dict(
        title= "RECOVERY",
        x=-0.05,
        y=0.9,
        title_font_family="Arial",
        font=dict(
            family="Arial",
            size=8,
            color="White"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=1
    ),

    legend2=dict(
        title="NUTRITION",
        x=0.35,
        y=0.90,
        title_font_family="Arial",
        font=dict(
            family="Arial",
            size=8,
            color="White"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=1
    ),

    legend3=dict(
        title="TRAINING",
        x=0.75,
        y=0.90,
        title_font_family="Arial",
        font=dict(
            family="Arial",
            size=8,
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
