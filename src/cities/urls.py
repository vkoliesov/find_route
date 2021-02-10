from django.urls import path

from cities.views import home

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/', home, name='detail')
]
