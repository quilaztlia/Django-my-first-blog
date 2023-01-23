from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    #https://docs.djangoproject.com/en/3.2/ref/models/querysets/
    posts = Post.objects.order_by('published_date')    
    #.filter(published_date__lte=timezone.now())
    

    return render(request, 'blog/post_list.html', {'posts': posts})
