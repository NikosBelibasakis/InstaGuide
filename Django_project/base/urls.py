from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('get_reviews/', views.get_reviews, name="get_reviews"), 
    path('get_query/', views.get_query, name='get_query'), 
    path('clear_reviews/', views.clear_reviews, name='clear_reviews'),
    path('cr_summ/', views.cr_summ, name='cr_summ'),
]
