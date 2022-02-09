from django.urls import path
from cities import views

urlpatterns = [
    path('', views.CityListView.as_view(), name='cities_list'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('add/', views.CityCreateView.as_view(), name='city_create'),
    path('update/<int:pk>/', views.CityUpdateView.as_view(), name='city_update'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='city_delete'),

]
