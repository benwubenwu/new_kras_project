from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ColonData
from plotly.offline import plot
import plotly.graph_objects as go
from django.http import HttpRequest
# Create your views here.

protein_id = "asdf"


def search(request):
    colon_data = ColonData.objects.all()
    context = {
        'colon_data': colon_data
    }
    return render(request, "graphs/search.html", context)


def search_results(request):
    colon_data = ColonData.objects.all()
    context = {
        'colon_data': colon_data
    }

    protein_id = request.POST.get('protein_id')
    print(protein_id)

    def get_protein_id():
        return protein_id

    return render(request, "graphs/search_results.html", context)


def graphs(request):
    print(protein_id)
    colon_data = ColonData.objects.all()
    gene1 = ColonData.objects.get(id=5)
    gene1name = gene1.gene_symbol
    gene1control1 = gene1.control1
    gene1control2 = gene1.control2
    gene1control3 = gene1.control3
    gene1control4 = gene1.control4
    gene1control5 = gene1.control5

    gene1kras1 = gene1.kras1
    gene1kras2 = gene1.kras2
    gene1kras3 = gene1.kras3
    gene1kras4 = gene1.kras4
    gene1kras5 = gene1.kras5
    # gene1 = ColonData.objects.get(id=1)
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
        y0 = [gene1control1, gene1control2,
              gene1control3, gene1control4, gene1control5]
        y1 = [gene1kras1, gene1kras2, gene1kras3, gene1kras4, gene1kras5]

        layout = dict(
            title=gene1name,
            template="plotly_white",
        )
        fig = go.Figure(layout=layout)
        fig.add_trace(go.Box(y=y0, name='Control',
                             marker_color='rgba(0, 102, 255, 1.0)', boxpoints='all'))
        fig.add_trace(go.Box(y=y1, name='Mutant',
                             marker_color='rgba(153, 204, 255, 1.0)', boxpoints='all'))
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot': box(),
        'colon_data': colon_data,
        'gene1name': gene1name

    }
    return render(request, "graphs/graphs.html", context)
