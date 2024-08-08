from django.urls import path, include 
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('add-recipe/', views.form_add, name="add_recipe"),
    path('add/', views.add, name="add")
]
