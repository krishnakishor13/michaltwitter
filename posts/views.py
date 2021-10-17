from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm

from cloudinary.forms import cl_init_js_callbacks


def index(request):
    
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
         print('hello world')
         form.save()
         return HttpResponseRedirect('/')
        else:
          return HttpResponseRedirect(form.errors.as_json())


    posts = Post.objects.all().order_by('-created_at')
    return render(request,'posts.html',
              {'posts':posts})

def delete(request,post_id):
     post=Post.objects.get(id=post_id)
     post.delete()
     return HttpResponseRedirect('/')

def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
          form=PostForm(request.POST,request.FILES,instance = post)
          
          if form.is_valid():
             post.save()
             return HttpResponseRedirect('/')
    else:
        form=PostForm(PostForm)
        return render(request,'edit.html',{'post':post, 'form':form})

#likes - 

def LikeView(request,post_id):
    post=Post.objects.get(id=post_id)
    new_value=post.likes +1
    post.likes=new_value
    post.save()
    return HttpResponseRedirect('/')


