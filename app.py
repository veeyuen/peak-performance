import streamlit as st
import plotly.graph_objects as go
import plotly.offline as pyo

categories = ['Weight', 'Sleep Length(hrs)', 'Sleep Quality[1-10]', 'Stress Management[1-10]', 'Mental Health[15-0]']
categories = [*categories, categories[0]]

Day_0 = [0, 5.5, 4, 3, 9.75]
Day_15 = [-1.9, 5.9, 4, 4, 5, 2]
Day_30 = [-4.0, 6.4, 7, 6, 0]
Day_0 = [*Day_0, Day_0[0]]
Day_15 = [*Day_15, Day_15[0]]
Day_30 = [*Day_30, Day_30[0]]


# Simple radar plot

fig = go.Figure(
    data=[
        go.Scatterpolar(r=Day_0, theta=categories, fill='toself', name='Day 0'),
        go.Scatterpolar(r=Day_15, theta=categories, fill='toself', name='Day 15'),
        go.Scatterpolar(r=Day_30, theta=categories, fill='toself', name='Day 30')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Peak Performance - Recovery'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

#if __name__ == '__main__':
#
#    pyo.plot(fig)


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
#    val = st.slider('Select value',0,10,1)
#    radar_chart(val)
