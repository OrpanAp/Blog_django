from .models import Category
from assignments.models import SocialConnect


def get_categories(request):
    categories = Category.objects.all().order_by('-created_at')
    return dict(categories=categories)

def get_socialConnects(request):
    socialConnects = SocialConnect.objects.all()
    return dict(socialConnects=socialConnects)