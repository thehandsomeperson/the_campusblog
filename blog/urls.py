from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #the url to post_list
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]