from django.shortcuts import render
from django.views.generic import TemplateView
from . import plots
from .models import ColonData
# Create your views here.


def graphs(request):
    colon_data = ColonData.objects.all()
    return render(request, "graphs/graphs.html", {'colon_data': colon_data})
