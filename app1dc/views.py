from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse('Hello django')

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Edjay Dela Cruz'})

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    each_post = Post.objects.all()
    context = {
        'blog_detail': each_post
    }
return render(request, 'blog_detail.html', context)