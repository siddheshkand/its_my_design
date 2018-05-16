from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Home.models import Category


def home_page(request):
    all_category = Category.objects.filter(is_active=True).order_by('rank')
    # num = 10
    # for each in all_category:
    #     each.rank = num
    #     each.save()
    #     num += 10
    return render(request, "home.html", {
        'all_category': all_category,
        'width_percent': 20
    })


def test_page(request):
    return render(request, "BusinessCard.html", {

    })