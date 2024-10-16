from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('get_reviews/', views.get_reviews, name="get_reviews"), 
]
