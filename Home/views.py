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


def work(request):
    # This code takes the path and gets the last part of url
    # ie. work/logo design => logo desin
    project_type_name = request.path
    project_type_name = project_type_name.split('/')

    # all category same as above
    all_category = Category.objects.filter(is_active=True)
    return render(request, "work.html", {
        'project_type_name': project_type_name[2],
        'all_category': all_category,
    })
