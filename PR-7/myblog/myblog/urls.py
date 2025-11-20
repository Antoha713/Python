from django import views
from django.contrib import admin
from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

]
