import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import random
from plotly.subplots import make_subplots


categories = ['Weight', 'Sleep Length(hrs)', 'Sleep Quality[1-10]', 'Stress Management[1-10]', 'Mental Health[15-0]']
categories = [*categories, categories[0]]

Day_0 = [0, 5.5, 4, 3, 9.75]
Day_15 = [-1.9, 5.9, 4, 4, 5, 2]
Day_30 = [-4.0, 6.4, 7, 6, 0]
Day_0 = [*Day_0, Day_0[0]]
Day_15 = [*Day_15, Day_15[0]]
Day_30 = [*Day_30, Day_30[0]]

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



fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'}] * 2] * 1)

fig.add_trace(
    go.Scatterpolar(
        theta=["Sleep Quality", "Stress Management", "Mental Health"],
        r=r1,
        fill='toself',
        name='Day 0',
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["Sleep Quality", "Stress Management", "Mental Health"],
        r=[3,9,4],
        fill='toself',
        name='Day 15',
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["Cognitive Function", "Sick Leave", "Energy Levels"],
        r=[5,6,3],
        fill='toself',
        name='Day 0',
    ),
    row=1,
    col=2,
)
fig.add_trace(
    go.Scatterpolar(
        theta=["Cognitive Function", "Sick Leave", "Energy Levels"],
        r=[3,9,4],
        fill='toself',
        name='Day 15',
    ),
    row=1,
    col=2,
)
#pyo.plot(fig)

fig.update_layout(
    autosize=False,
    minreducedwidth=450,
    minreducedheight=450,
    width=650,
    height=650,
    
polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),

    title=go.layout.Title(text='Peak Performance - XXXX'),
    polar={'radialaxis': {'visible': True}},
  showlegend=True
)


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
