from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles, name='profiles'),
    path('profiles/<int:blogger_id>/', views.profile_details, name='profile_details'),

    path('news/', views.news, name='news'),

    path('news/', views.redirect_to_home, name='news'),
]
