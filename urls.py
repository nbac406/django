from django.urls import path, include
from . import views
#from .views import Category, Post


urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:post_id>/', views.post, name = 'post'),
    path('question/create/', views.post_create, name = 'post_create'),
    #path('post_create', views.post_create, name = 'post_create'),
]