from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [

    # / - Home Page
    url(r'^$', views.home_page, name='home_page'),
    url('^work/', views.work, name='work'),
    url('^about/', views.about, name='about'),
    url('^contact/', views.contact, name='contact'),
    url('^404/',views.page_not_found,name='404'),
    url('^voting/',views.voting,name='voting')
]
