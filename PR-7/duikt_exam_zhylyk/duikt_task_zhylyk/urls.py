from django.urls import path
from .views import install, show_cars

urlpatterns = [
    path('install/', install),
    path('duikt_page_zhylyk/', show_cars),
]
