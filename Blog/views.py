from django.shortcuts import render,redirect
from .models import blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home_page(request):
    blog_list=blog.objects.all()
    print(blog_list)
    context={'blog_list':blog_list}
    return render(request,'home.html',context)

@login_required
def add_blog(request):
    if request.method=='POST':
        title=request.POST['title'].strip()
        content=request.POST['content'].strip()
        sub_title=request.POST['subtitle'].strip()

        if not title :
            messages.error(request,'Enter title to save')
            return redirect('add_blog')
        
        if not content:
            messages.error(request,'Enter content to save')
            return redirect('add_blog')
        if not sub_title:
            messages.error(request,'Enter sub_title to save')
            return redirect('add_blog')
        
        blog.objects.create(title=title, sub_title=sub_title,content=content,related_user=request.user)
        messages.success(request,'blog post added succesfully')
        return redirect('add_blog')
    return render(request,'addblog.html')

@login_required
def profile(request,id=None):
    print(request.user)
    user=User.objects.get(id=id)
    all_blog=blog.objects.filter(related_user=id)
    context={
        'seluser':user,
        "allblog":all_blog
    }
    return render(request,'profile.html' ,context)

@login_required
def full_blog(request,id):
    print(id)
    selected_blog=blog.objects.get(id=id)
    print(selected_blog)
    context={
        
        'selected_blog':selected_blog
    }
    return render(request,'fullblog.html',context)

@login_required
def delete_blog(request, id):
    selblog = blog.objects.get(id=id)
    selblog.delete()
    return redirect('profile',id=request.user.id)