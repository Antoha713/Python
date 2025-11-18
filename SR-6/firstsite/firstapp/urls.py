from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles, name='profiles'),
    path('news/', views.redirect_to_home, name='news'),
    path('news-page/', views.news_page, name='news_page'),

    path('profiles/<int:blogger_id>/', views.profile_details, name='profile_details')
]
