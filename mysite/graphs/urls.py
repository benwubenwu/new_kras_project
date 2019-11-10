from django.urls import path
from graphs import views
# from .views import SimpleCandlestickWithPandas
urlpatterns = [
    path('', views.graphs, name='graphs'),
]
