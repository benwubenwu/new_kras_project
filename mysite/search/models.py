# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import plotly.express as px
# import plotly.graph_objects as go
from django.db import models

# Create your models here.


class Protein(models.Model):
    protein_text = models.CharField(max_length=200)

    # @property
    # def graph(self):
    #     fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    #     fig.show()
