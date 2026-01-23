from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs, Category
from django.db.models import Q


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

def blogs(request, slug):
    post = get_object_or_404(Blogs, slug=slug, status='Published')
    data = {
        'blog': post,
    }
    return render(request, 'blogs.html', data)


def search(request):
    search_term = request.GET.get("search_term", "").strip()

    results = Blogs.objects.none()  # empty queryset by default

    if search_term:
        results = Blogs.objects.filter(
            Q(title__icontains=search_term)
            | Q(short_description__icontains=search_term)
            | Q(blog_body__icontains=search_term)
            | Q(author__username__icontains=search_term)
            | Q(category__category_name__icontains=search_term),
            status="Published"
        )

    data = {
        'results': results,
        'search_term': search_term,
    }

    return render(request, "search_results.html", data)
