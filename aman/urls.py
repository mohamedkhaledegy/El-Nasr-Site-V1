from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index , name='home' ),
    path('stores/', views.store_list , name='stores' ),
    path('store/<slug:slug>/', views.store_detail , name='store_detail' ),
    path('new-request/', views.new_request , name='new_request' ),
]