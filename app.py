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
np.random.seed(1)

#images_folder = '/Users/veesheenyuen/Desktop/DataScience/Peak/'
#image_path = images_folder/peak-logo.png

#main_image = Image.open('/Users/veesheenyuen/Desktop/peak-logo.png')
#st.image (main_image) 

N = 100
random_x = np.linspace(0, 300, N)
random_y0 = np.random.randn(N) 
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) 


#categories = ['Weight', 'Sleep Length(hrs)', 'Sleep Quality[1-10]', 'Stress Management[1-10]', 'Mental Health[15-0]']
#categories = [*categories, categories[0]]

#Day_0 = [0, 5.5, 4, 3, 9.75]
#Day_15 = [-1.9, 5.9, 4, 4, 5, 2]
#Day_30 = [-4.0, 6.4, 7, 6, 0]
#Day_0 = [*Day_0, Day_0[0]]
#Day_15 = [*Day_15, Day_15[0]]
#Day_30 = [*Day_30, Day_30[0]]

r1 =[5,6,3,8,5]

# Simple radar plot

#fig = go.Figure(
#    data=[
#        go.Scatterpolar(r=Day_0, theta=categories, fill='toself', name='Day 0'),
#        go.Scatterpolar(r=Day_15, theta=categories, fill='toself', name='Day 15'),
#        go.Scatterpolar(r=Day_30, theta=categories, fill='toself', name='Day 30')
#    ],
#    layout=go.Layout(
#        title=go.layout.Title(text='Peak Performance - XXXX'),
#        polar={'radialaxis': {'visible': True}},
#        showlegend=True
#    )
#)

#if __name__ == '__main__':



#fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'polar'}] * 2] * 1, horizontal_spacing = 0.20)

xaxis_title="Miliseconds"
yaxis_title="Services"

fig = make_subplots(
    rows=4, cols=2,
    specs=[[{"type": "polar"}, {"type": "polar"}],
           [{"type": "scatter"}, {"type": "scatter"}],
           [{"type": "polar"}, {"type": "scatter", "rowspan": 2}],
           [{"type": "scatter"}, None]          
              ], 
    horizontal_spacing= 0.20, row_heights=[0.7, 0.3, 0.7, 0.3]
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
        theta=["<b>Sleep<br>Quality<b>", "<b>Stress<br>Management<b>", "<b>Mental<br>Health<b>"],
        r=[3,9,4],
        fill='toself',
        name='Day 15',
        legend="legend1"
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Cognitive<br>Function<b>", "<b>Sick<br>Leaves<b>", "<b>Energy<br>Levels<b>"],
        r=[5,6,3],
        fill='toself',
        name='Day 0',
        legend="legend2"
    ),
    row=1,
    col=2,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Cognitive<br>Function<b>", "<b>Sick<br>Leaves<b>", "<b>Energy<br>Levels<b>"],
        r=[3,9,4],
        fill='toself',
        name='Day 15',
        legend="legend2"
    ),
    row=1,
    col=2,
)

fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Levek<b>", "<b>Stamina<b>"],
        r=[2,5,8],
        fill='toself',
        name='Day 0',
        legend="legend2"
    ),
    row=3,
    col=1,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["<b>Activity<br>Level<b>", "<b>Strength<br>Levek<b>", "<b>Stamina<b>"],
        r=[7,3,9],
        fill='toself',
        name='Day 15',
        legend="legend2"
    ),
    row=3,
    col=1,
)


fig.add_trace(
    go.Scatter(
        x=random_x, y=random_y0,
        mode='lines+markers',
        name='Time (Days)',
        showlegend=False
    ),
    row=2,
    col=1,
    
    )

fig.add_trace(
    go.Scatter(
        x=random_x, y=random_y1,
        mode='lines+markers',
        name='Time (Days)',
        showlegend=False
    ),
    row=2,
    col=2,


)

#pyo.plot(fig)

fig.update_layout(
    autosize=False,
#    minreducedwidth=350,
#    minreducedheight=350,
    width=850,
    height=850,
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

#    yaxis_title = 'Stress<br>Activity',
#    xaxis_title = 'Days',

  showlegend=True
)

fig.update_polars(
    radialaxis=dict(
        angle=45
    )
)

fig.update_xaxes(title_text="Days", row=2, col=1)
fig.update_yaxes(title_text="Recovery<br>Activity", row=2, col=1)
fig.update_xaxes(title_text="Days", row=2, col=2)
fig.update_yaxes(title_text="Nutrition<br>Activity", row=2, col=2)



#fig.update_traces(mode = "lines+markers",
#      r = [1,2,3,4,5],
#      theta = [0,90,180,360,0],
#      line_color = "magenta",
#      marker = dict(
#        color = "royalblue",
#        symbol = "square",
#        size = 8
#      ))



#fig.update_xaxes(automargin=True)

#fig.update_traces(fill = 'toself', textposition = 'top center'),
st.plotly_chart(fig)


#fig = make_subplots(rows=1, cols=2, specs=[[{"type": "barpolar"}, {"type": "barpolar"}],
#           )

#fig.add_trace(go.Barpolar(r=Day_0, theta=categories, name='Day 0'),row=1, col=1)

#fig.add_trace(go.Barpolar(r=Day_15, theta=categories, name='Day 15'),row=1, col=2)

#pyo.plot(fig)
#st.plotly_chart(fig)



#def radar_chart(val):
#    df = pd.DataFrame(dict(
#    r=[random.randint(0,val),
#       random.randint(0,val),
#       random.randint(0,val),
#       random.randint(0,val)],
#    theta=['Sleep Length(hr)','Sleep Quality[1-10]','Stress Mgmt[1-10]',
#           'Mental Health 4x']))
#    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
#    st.write(fig)


#if __name__ == '__main__':
#val = st.slider('Select value',0,10,1)
#radar_chart(val)
