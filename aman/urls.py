from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index , name='home' ),
    path('stores/', views.store_list , name='stores' ),
]