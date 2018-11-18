from django.urls import path

from . import views

urlpatterns = [
    path('your-name/', views.get_name),
    path('thanks/', views.get_name),
    path('', views.index),
]
