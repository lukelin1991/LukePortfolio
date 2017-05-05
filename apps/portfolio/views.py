from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def about(request):
    return render(request, 'portfolio/about.html')

def cssdesign(request):
    return render(request, 'portfolio/cssdesign.html')
