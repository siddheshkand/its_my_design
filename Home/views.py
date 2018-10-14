from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from Home.models import Category, Query
from django.conf import settings

from django.core.mail import send_mail


def home_page(request):
    all_category = Category.objects.filter(is_active=True).order_by('rank')
    return render(request, "home.html", {
        'all_category': all_category,
        'width_percent': 20
    })


def work(request):
    category = request.GET.get('category')
    # all category same as above
    category_obj = get_object_or_404(Category, name=category)
    projects = category_obj.project_set.all()
    if projects.__len__() == 0:
        return render(request, 'election_campaign.html', {
            'category': category_obj
        })
    # projects = sorted(projects,key=lambda x:x.rank)
    # print(category_obj.text)
    return render(request, "work.html", {
        'project_type_name': category_obj,
        'all_category': projects,
    })


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def page_not_found(request):
    return render(request, '404.html')


def voting(request):
    return render(request, 'voting.html')


def query(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        obj = Query.objects.create(email=email, first_name=fname, last_name=lname, subject=subject,
                                   description=description)

        message = "<h3>You have query received from " + fname + " " + lname + ".</h3>"
        message += "<h3>And has provided this mail for communication<h3>" + email + "<h2>Description : </h2><0=h2>" + description + "</h2>"
        obj.save()
        send_mail(subject,
                  message,
                  email,
                  ['itsmydesignbrand@gmail.com'], fail_silently=False, html_message=message)
        return redirect('/contact/')

    else:
        return HttpResponse('Something went wrong')
