from django.urls import path
from graphs import views
# from mysite.graphs.dash_apps.finished_apps import boxplot
urlpatterns = [
    path('', views.graphs, name='graphs'),
]
