from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    url(r'^test$', views.test_page, ),

    # / - Home Page
    url(r'^$', views.home_page, name='home_page'),
    url('^work/', views.work, name='work')
]
