import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import random


categories = ['Weight', 'Sleep Length(hrs)', 'Sleep Quality[1-10]', 'Stress Management[1-10]', 'Mental Health[15-0]']
categories = [*categories, categories[0]]

Day_0_1 = [0, 5.5, 4, 3, 9.75]
Day_15_1 = [-1.9, 5.9, 4, 4, 5, 2]
Day_3_1 = [-4.0, 6.4, 7, 6, 0]
Day_0_1 = [*Day_0_1, Day_0_1[0]]
Day_15_1 = [*Day_15_1, Day_15_1[0]]
Day_30_1 = [*Day_30_1, Day_30_1[0]]


# Simple radar plot

fig1 = go.Figure(
    data=[
        go.Scatterpolar(r=Day_0_1, theta=categories, fill='toself', name='Day 0'),
        go.Scatterpolar(r=Day_15_1, theta=categories, fill='toself', name='Day 15'),
        go.Scatterpolar(r=Day_30_1, theta=categories, fill='toself', name='Day 30')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Peak Performance - Recovery'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

#if __name__ == '__main__':

#pyo.plot(fig)
st.plotly_chart(fig1)



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
