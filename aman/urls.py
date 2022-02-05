from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index , name='home' ),
    path('stores/', views.store_list , name='stores' ),
    path('stores/<slug:slug>/', views.store_detail , name='store_detail' ),
    path('stores/<slug:slug>/new-request/', views.new_request , name='new_request' ),
    path('visit/new/', views.new_visit , name='new_visit' ),
    path('visit/list/', views.visit_list , name='visit_list' ),
    path('<slug:slug>/visit/list/', views.visit_list_store , name='visit_list_store' ),
]