from django.urls import path
from graphs import views
from graphs.dash_apps.finished_apps import simpleexample
# from mysite.graphs.dash_apps.finished_apps import boxplot
urlpatterns = [
    path('', views.graphs, name='graphs'),
    path('search', views.search, name='test')
]
