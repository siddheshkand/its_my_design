from django.contrib.auth.models import User
from django.db import models


def category_icon_path(instance, filename):
    return 'Media/Categories/{0}/{1}'.format(instance.name, filename)


class DayHit(models.Model):
    hits = models.IntegerField(default=0)
    date = models.DateField()


class SiteDetail(models.Model):
    total_hits = models.BigIntegerField(default=0)


class Log(models.Model):
    user = models.ForeignKey(User)
    time_stamp = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField()
    logo = models.ImageField(upload_to=category_icon_path)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + str(self.number) + str(self.email)
