from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoriesForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    categories_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()

    data = {
        'categories_count': categories_count,
        'blogs_count': blogs_count, 
    }
    return render(request, 'dashboard/dashboard.html', data)

@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
def add_categories(request):

    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoriesForm()

    data = {
        'form': form,
    }

    return render(request, 'dashboard/add_categories.html', data)


@login_required(login_url='login')
def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoriesForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoriesForm(instance=category)

    data = {
        'form': form,
        'category': category,
    }

    return render(request, 'dashboard/edit_categories.html', data)

@login_required(login_url='login')
def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
