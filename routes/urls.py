from django.urls import path
from routes import views

urlpatterns = [
    path('', views.RouteFindView.as_view(), name='home'),
    path('find_routes/', views.find_routes, name='find_routes'),
    path('add_route/', views.add_route, name='add_route'),
    path('save_route/', views.save_route, name='save_route'),
    path('list/', views.RouteListView.as_view(), name='routes_list'),
    path('detail/<int:pk>/', views.RouteDetailView.as_view(), name='route_detail'),
    path('delete/<int:pk>/', views.RouteDeleteView.as_view(), name='route_delete'),
]
