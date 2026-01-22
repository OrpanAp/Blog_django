from django.shortcuts import render
from blogs.models import Blogs

def home(request):
    all_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('-created_at')

    data = {
        'featured_post': all_posts.first(),
        'posts': all_posts.exclude(pk=all_posts.first().pk),
        'other_posts': Blogs.objects.filter(is_featured=False, status='Published'),
    }

    return render(request, 'home.html', data)