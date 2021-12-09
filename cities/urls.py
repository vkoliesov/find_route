from django import views
from django.urls import path
from cities import views

urlpatterns = [
    path('', views.CityListView.as_view(), name='cities_list'),
    path('<int:city_id>/', views.CityDetailView.as_view(), name='city_detail'),

]
