from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #the url to post_list
    path('', views.post_list, name='post_list'),
]