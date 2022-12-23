from django.urls import path
from blog.views import addPosts,viewPost
urlpatterns =[
    path('post/add',addPosts),
    path('post/',viewPost)
]