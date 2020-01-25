from django.urls import path, re_path
from graphs import views
from graphs.dash_apps.finished_apps import simpleexample
# from mysite.graphs.dash_apps.finished_apps import boxplot
urlpatterns = [
    path('graphs', views.graphs, name='graphs'),
    path('search_results', views.search_results, name="search_results"),
    path('', views.search, name='search'),
    path('test/<int:id>', views.graphs, name='test'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]
