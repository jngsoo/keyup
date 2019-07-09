
from django.contrib import admin
from django.urls import path
from mainpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('/result', views.result, name="result"),
    
    path('/graph_1', views.graph_1, name="graph_1"),
    path('/graph_2', views.graph_2, name="graph_2"),
    path('/graph_3', views.graph_3, name="graph_3"),
    path('/graph_4', views.graph_4, name="graph_4"),

]
