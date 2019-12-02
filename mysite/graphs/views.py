from django.shortcuts import render
from django.views.generic import TemplateView
from . import plots
from .models import Colon
# Create your views here.


def graphs(request):
    colon_data = Colon.objects.all()
    return render(request, "graphs/graphs.html", {'colon_data': colon_data})


# class BoxPlot(TemplateView):
#     template_name = 'plot.html'

#     def get_context_data(self, **kwargs):
#         context = super(BoxPlot, self).get_context_data(**kwargs)
#         context['boxplot'] = plots.get_box_plot()
#         return context
