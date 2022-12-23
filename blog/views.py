from django.shortcuts import render
from blog.forms import PostForm
from django.http import HttpResponse
from blog.models import Post
from django.db.models import Q

# Create your views here.

def addPosts(request):
    if request.method == "POST":
        aPost  = PostForm(request.POST)
        if aPost.is_valid():
            aPost = aPost.save(commit=False)
            aPost.author = request.user.profile
            aPost.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('error')
    else:
        form=PostForm()
        return render(request,'post_add.html',{'form':form})
    

def viewPost(request):
    q=request.GET.get('q')
    if q:
        posts=Post.objects.filter(
            Q(title__contains=q) | Q(text__contains=q)
        ).order_by('-created_date')
    else:
        posts = Post.objects.all().order_by('-created_date')
    return render(request,'view_posts.html',{'posts':posts ,'title':'all posts','search':q})

    

