from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from blog.models import post

def frontpage(request):
#    posts = post.objects.all()
    posts = post.objects.filter(status=post.ACTIVE)
    
    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /Admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

