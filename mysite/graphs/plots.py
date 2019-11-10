from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
import requests


def get_data():
    url = 'https://api.unibit.ai/historicalstockprice/AAPL?range=3m&interval=2&AccessKey=demo'
    res = requests.get(url)
    res = res.json()['Stock price']
    return res


# def get_simple_candlestick():
#     data = pd.read_csv(
#         "/Users/benjaminwu/Desktop/kras_project/csv/2017-03-19_Haigis_5v5_Pro copy.csv")

#     layout = go.Layout(
#         # autosize=True,
#         # width = 800,
#         # height=900,
#         xaxis=dict(
#             autorange=True
#         ),
#         yaxis=dict(
#             autorange=True
#         )
#     )

#     figure = go.Figure(data=plot_data, layout=layout)
#     plot_div = plot(figure, output_type='div', include_plotlyjs=False)
#     return plot_div
