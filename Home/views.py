from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Home.models import Category


def home_page(request):
    all_category = Category.objects.filter(is_active=True)
    return render(request, "home.html", {
        'all_category': all_category,
        'width_percent': 20
    })
