from .models import Category

def get_categories(request):
    categories = Category.objects.all().order_by('-created_at')
    return dict(categories=categories)