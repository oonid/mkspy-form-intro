from django.urls import path

from . import views

urlpatterns = [
    path('your-name/', views.get_name),
    path('thanks/', views.get_name),
    path('friend-data/', views.friend_data_form, name='friend-form'),
    path('', views.index),
]
