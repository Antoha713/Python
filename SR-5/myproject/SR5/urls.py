from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_table, name='profile_table'),
]
