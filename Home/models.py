from django.contrib.auth.models import User
from django.db import models


def category_icon_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    name = instance.name
    name = name.replace(" ", "")
    return 'Media/Categories/{0}/{1}.{2}'.format(name, name, extension)


def project_media_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    name = instance.name
    name = name.replace(" ", "")
    return 'Media/Categories/{0}/{1}/{2}.{3}'.format(instance.category.name, name, name, extension)


class DayHit(models.Model):
    hits = models.IntegerField(default=0)
    date = models.DateField()


class SiteDetail(models.Model):
    total_hits = models.BigIntegerField(default=0)


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField()
    logo = models.ImageField(upload_to=category_icon_path)
    rank = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name + ' ' + str(self.rank)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    media = models.ImageField(upload_to=project_media_path)

    def __str__(self):
        return self.category.name + '-' + self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + str(self.number) + str(self.email)
