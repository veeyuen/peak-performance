import streamlit as st
import plotly.express as px
import pandas as pd
import random

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

if __name__ == '__main__':

    pyo.plot(fig)

# Complex radar plot with different axes

class ComplexRadar():
    """
    Create a complex radar chart with different scales for each variable
    Parameters
    ----------
    fig : figure object
        A matplotlib figure object to add the axes on
    variables : list
        A list of variables
    ranges : list
        A list of tuples (min, max) for each variable
    n_ring_levels: int, defaults to 5
        Number of ordinate or ring levels to draw
    show_scales: bool, defaults to True
        Indicates if we the ranges for each variable are plotted
    """
    def __init__(self, fig, variables, ranges, n_ring_levels=5, show_scales=True):
        # Calculate angles and create for each variable an axes
        # Consider here the trick with having the first axes element twice (len+1)
        angles = np.arange(0, 360, 360./len(variables))
        axes = [fig.add_axes([0.1,0.1,0.9,0.9], polar=True, label = "axes{}".format(i)) for i in range(len(variables)+1)]

        # Ensure clockwise rotation (first variable at the top N)
        for ax in axes:
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            ax.set_axisbelow(True)

        # Writing the ranges on each axes
        for i, ax in enumerate(axes):

            # Here we do the trick by repeating the first iteration
            j = 0 if (i==0 or i==1) else i-1
            ax.set_ylim(*ranges[j])
            # Set endpoint to True if you like to have values right before the last circle
            grid = np.linspace(*ranges[j], num=n_ring_levels,
                               endpoint=False)
            gridlabel = ["{}".format(round(x,2)) for x in grid]
            gridlabel[0] = "" # remove values from the center
            lines, labels = ax.set_rgrids(grid, labels=gridlabel, angle=angles[j])

            ax.set_ylim(*ranges[j])
            ax.spines["polar"].set_visible(False)
            ax.grid(visible=False)

            if show_scales == False:
                ax.set_yticklabels([])

        # Set all axes except the first one unvisible
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.xaxis.set_visible(False)

        # Setting the attributes
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]
        self.ax1 = axes[1]
        self.plot_counter = 0

        # Draw (inner) circles and lines
        self.ax.yaxis.grid()
        self.ax.xaxis.grid()

        # Draw outer circle
        self.ax.spines['polar'].set_visible(True)

        # ax1 is the duplicate of axes[0] (self.ax)
        # Remove everything from ax1 except the plot itself
        self.ax1.axis('off')
        self.ax1.set_zorder(9)

        # Create the outer labels for each variable
        l, text = self.ax.set_thetagrids(angles, labels=variables)

        # Beautify them
        labels = [t.get_text() for t in self.ax.get_xticklabels()]
        labels = ['\n'.join(textwrap.wrap(l, 15,
                                          break_long_words=False)) for l in labels]
        self.ax.set_xticklabels(labels)

        for t,a in zip(self.ax.get_xticklabels(),angles):
            if a == 0:
                t.set_ha('center')
            elif a > 0 and a < 180:
                t.set_ha('left')
            elif a == 180:
                t.set_ha('center')
            else:
                t.set_ha('right')

        self.ax.tick_params(axis='both', pad=15)


    def _scale_data(self, data, ranges):
        """Scales data[1:] to ranges[0]"""
        for d, (y1, y2) in zip(data[1:], ranges[1:]):
            assert (y1 <= d <= y2) or (y2 <= d <= y1)
        x1, x2 = ranges[0]
        d = data[0]
        sdata = [d]
        for d, (y1, y2) in zip(data[1:], ranges[1:]):
            sdata.append((d-y1) / (y2-y1) * (x2 - x1) + x1)
        return sdata

    def plot(self, data, *args, **kwargs):
        """Plots a line"""
        sdata = self._scale_data(data, self.ranges)
        self.ax1.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kwargs)
        self.plot_counter = self.plot_counter+1

    def fill(self, data, *args, **kwargs):
        """Plots an area"""
        sdata = self._scale_data(data, self.ranges)
        self.ax1.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kwargs)

    def use_legend(self, *args, **kwargs):
        """Shows a legend"""
        self.ax1.legend(*args, **kwargs)

    def set_title(self, title, pad=25, **kwargs):
        """Set a title"""
        self.ax.set_title(title,pad=pad, **kwargs)



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
