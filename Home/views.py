from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from Home.models import Category


def home_page(request):
    all_category = Category.objects.filter(is_active=True)
    return render(request, "home.html", {
        'all_category': all_category,
        'width_percent': 20
    })


def work(request):
    category = request.GET.get('category')
    # all category same as above
    category_obj = get_object_or_404(Category, name=category)
    projects = category_obj.project_set.all()
    return render(request, "work.html", {
        'project_type_name': category,
        'all_category': projects,
    })


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
