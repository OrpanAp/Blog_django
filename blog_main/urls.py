from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from blogs import views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blogs/search/', blogViews.search, name ='search'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', blogViews.blogs, name ='blogs'),
    path('register/', views.register, name ='register'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
    path('dashboard/', include('dashboard.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    