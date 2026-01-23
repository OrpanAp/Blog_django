from django.shortcuts import render, redirect
from blogs.models import Blogs
from assignments.models import About, SocialConnect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Account created successfully! You can now log in.")
            return redirect('register')
        else:
            messages.error(request, "❌ Please fix the errors below.")

    else:
        form = RegistrationForm() 


    data = { 
        'form': form 
    }

    return render(request, 'register.html', data)

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                
                messages.success(request, f"👋 Welcome back, {user.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "❌ Invalid username or password.")

    data = {
        'form': form,
    }

    return render(request, 'login.html', data)

def logout(request):
    auth.logout(request)
    messages.info(request, "👋 You have been logged out successfully.")
    return redirect('login')