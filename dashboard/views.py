from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoriesForm, BlogPostForm, AddUserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import messages


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


@login_required(login_url='login')
def posts(request):
    posts = Blogs.objects.all()

    data = {
        'posts': posts,
    }

    return render(request, 'dashboard/posts.html', data)


@login_required(login_url='login')
def add_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')
                
        else:
            print(form.errors)

    form = BlogPostForm()
    
    data = {
        'form': form,
    }

    return render(request, 'dashboard/add_posts.html', data)


@login_required(login_url='login')
def edit_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save()
            return redirect('posts')

    form = BlogPostForm(instance=post)

    data = {
        'form': form,
        'post': post,
    }

    return render(request, 'dashboard/edit_posts.html', data)

@login_required(login_url='login')
def delete_posts(request, pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')

@login_required(login_url='login')
def users(request):
    users = User.objects.all()

    data = {
        'users': users,    
    }
    return render(request, 'dashboard/users.html', data)


@login_required(login_url='login')
def add_users(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()

    data = {
        'form': form,
    }
    return render(request, 'dashboard/add_users.html', data)


@login_required(login_url='login')
def edit_users(request, pk):
    user = get_object_or_404(User, pk=pk)

    # 🚫 Block non-superusers from editing superusers
    if user.is_superuser and not request.user.is_superuser:
        messages.error(request, "❌ You are not allowed to edit a superuser.")
        return redirect('users')  # or 'dashboard' or 'home'

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users')

    form = EditUserForm(instance=user)
    
    data = {
        'form': form,
    }
    return render(request, 'dashboard/edit_users.html', data)


@login_required(login_url='login')
def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)

    # 🚫 Block non-superusers from editing superusers
    if user.is_superuser and not request.user.is_superuser:
        messages.error(request, "❌ You are not allowed to delete a superuser.")
        return redirect('users')  # or 'dashboard' or 'home'

    user.delete()
    messages.success(request, "✅ User deleted successfully.")
    return redirect('users')


