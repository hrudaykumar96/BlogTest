from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        blogs = Blogs.objects.all().order_by('-id')
        return render(request,'home.html', {'blogs':blogs})
    else:
        return redirect('login')

@login_required(login_url='login')   
def createBlogs(request):
    if not request.user.is_superuser:
        messages.warning(request,'You are not authorised to perform this action')
        return redirect('home')
    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            images = request.FILES.get('images')
            queryset = Blogs.objects.create(title=title, description=description, images=images)
            queryset.save()
            messages.success(request, 'Blog created successfully')
            return redirect('home')
        return render(request, 'home.html')
    


@login_required(login_url='login')   
def updateBlogs(request):
    if not request.user.is_superuser:
        messages.warning(request,'You are not authorised to perform this action')
        return redirect('home')
    else:
        if request.method == 'POST':
            id = request.POST.get('id')
            title = request.POST.get('title')
            description = request.POST.get('description')
            
            images = request.FILES.get('images')
            blog = get_object_or_404(Blogs, id=id)
            blog.title = title
            blog.description = description
            if images:
                blog.images = images
            else:
                blog.images = blog.images
            blog.save()
            messages.success(request, 'Blog Updated Successfully')
            return redirect('home')
        return render(request, 'home.html')
    

@login_required(login_url='login')
def deleteBlog(request):
    if not request.user.is_superuser:
        messages.warning(request,'You are not authorised to perform this action')
        return redirect('home') 
    if request.method == "POST":
        id = request.POST.get('id')
        blog = get_object_or_404(Blogs, id=id)
        blog.delete()
        messages.success(request,'Blog Deleted Successfully')
        return redirect('home')