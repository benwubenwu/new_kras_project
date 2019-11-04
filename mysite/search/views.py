# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Protein
# Create your views here.


def index(request):
    template = loader.get_template('search/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
