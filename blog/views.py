from django.shortcuts import render
from .models import Blog

def homeView(request):
    context = { 'blogs': Blog.objects.all() }
    template_name = 'home.html'
    return render(request,template_name,context)

def detailView(request,id):
    context = { 'blog': Blog.objects.filter(id=id).first() }
    template_name = 'detail.html'
    return render(request,template_name,context)
