from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:pk>/', views.place_detail, name='place_detail'),
]
