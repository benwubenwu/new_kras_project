from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from datetime import datetime
import requests
from .models import ColonData


# def get_data():
#     control1 = Colon[1].control1
#     control2 = Colon[1].control2
#     control3 = Colon[1].control3
#     control4 = Colon[1].control4
#     control5 = Colon[1].control5
#     return


def get_box_plot():
    # control1 = Colon[1].control1
    # control2 = Colon[1].control2
    # control3 = Colon[1].control3
    # control4 = Colon[1].control4
    # control5 = Colon[1].control5
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=[2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51,
           0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
        name='Only Mean',
        marker_color='darkblue',
        boxmean=True  # represent mean
    ))
    fig.add_trace(go.Box(
        y=[2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51,
           0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
        name='Mean & SD',
        marker_color='royalblue',
        boxmean='sd'  # represent mean and standard deviation
    ))
    fig = go.Figure()
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div


# fig.add_trace(go.Box(
#     y=[Colon.control1, Colon[10].control2, Colon[10].control3,
#         Colon[10].control4, Colon[10].control5],
#     name='Only Mean',
#     marker_color='darkblue',
#     boxmean=True  # represent mean
# ))
# fig.add_trace(go.Box(
#     y=[Colon[10].kras1, Colon[10].kras2, Colon[10].kras3,
#         Colon[10].kras4, Colon[10].kras5],
#     name='Mean & SD',
#     marker_color='royalblue',
#     boxmean='sd'  # represent mean and standard deviation
# ))
