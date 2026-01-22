from django.shortcuts import render, redirect
from .models import Blogs, Category


# Create your views here.
def post_by_category(request, category_id):
    #Fetch post with categoy id
    posts = Blogs.objects.filter(status='Published', category=category_id)

    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    data = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'post_by_category.html', data)