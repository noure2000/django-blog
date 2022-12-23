from django.urls import path
from blog.views import addPosts,viewPost,index
urlpatterns =[
    
    path('post/add',addPosts),
    path('post/',viewPost),
    path('home/',index),
]