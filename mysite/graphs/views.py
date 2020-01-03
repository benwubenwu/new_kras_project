from django.shortcuts import render
from django.views.generic import TemplateView
# from . import plots
from .models import ColonData
from plotly.offline import plot
import plotly.graph_objects as go
# Create your views here.


def graphs(request):
    colon_data = ColonData.objects.all()

    # def scatter():
    #     x1 = [1, 2, 3, 4]
    #     y1 = [30, 35, 25, 45]

    #     trace = go.Scatter(
    #         x=x1,
    #         y=y1
    #     )
    #     layout = dict(
    #         title='Simple Graph',
    #         xaxis=dict(range=[min(x1), max(x1)]),
    #         yaxis=dict(range=[min(y1), max(y1)]),
    #     )
    #     fig = go.Figure(data=[trace], layout=layout)
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    #     return plot_div

    def box():
        y0 = [1, 3, 5, 7, 9, 11]
        y1 = [2, 4, 6, 8, 10, 12]

        layout = dict(
            title='Simple Boxplot',
        )
        fig = go.Figure(layout=layout)
        fig.add_trace(go.Box(y=y0, name='Sample A', marker_color='indianred'))
        fig.add_trace(go.Box(y=y1, name='Sample B',
                             marker_color='lightseagreen'))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot': box(),
        'colon_data':  colon_data
    }
    return render(request, "graphs/graphs.html", context)
    # return render(request, "graphs/graphs.html", {'colon_data': colon_data})
