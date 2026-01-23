from django.shortcuts import render
from blogs.models import Blogs
from assignments.models import About, SocialConnect

def home(request):
    all_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('-created_at')

    try:
        about = About.objects.get()
    except:
        about=None
        
    data = {
        'featured_post': all_posts.first(),
        'posts': all_posts.exclude(pk=all_posts.first().pk),
        'other_posts': Blogs.objects.filter(is_featured=False, status='Published'),
        'about': about,
    }

    return render(request, 'home.html', data)