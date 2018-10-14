from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def category_icon_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    test = instance.name
    name = ''.join(e for e in test if e.isalnum())
    # print(name)
    return 'Media/Categories/{0}/{1}.{2}'.format(name, name, extension)


def thumbnail_category_icon_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    name = instance.name
    name = name.replace(" ", "")
    return 'Media/Categories/{0}/{1}.{2}'.format(name, name, extension)


def project_media_path(instance, filename):
    extension = filename.split('.')
    extension = extension[len(extension) - 1]
    name = instance.name
    name = ''.join(e for e in name if e.isalnum())
    return 'Media/Categories/{0}/{1}/{2}.{3}'.format(''.join(e for e in instance.category.name if e.isalnum()), name,
                                                     name,
                                                     extension.lower())


class Carousel(models.Model):
    name = models.CharField(max_length=50, null=True)


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
    text = models.TextField(null=True)

    def __str__(self):
        return self.name + ' ' + str(self.rank)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    media = models.FileField(upload_to=project_media_path, default=None, blank=True)
    media_type = models.BooleanField(default=0)
    youtube_url = models.URLField(null=True, blank=True)

    def clean(self):

        if self.youtube_url:
            self.media_type == 1
        else:
            video_extensions = ['mp4', 'mov', 'avi', 'mpg', 'wmv']
            image_extensions = ['jpeg', 'jpg', 'pnndfghjg']
            extension = self.media.name.split('.')
            extension = extension[len(extension) - 1]
            if extension.lower() in video_extensions:
                self.media_type = 1
            elif extension.lower() in image_extensions:
                self.media_type = 0
            else:
                raise ValidationError(u'Unsupported file extension.')

    def __str__(self):
        return self.category.name + '-' + self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + str(self.number) + str(self.email)


class Query(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
