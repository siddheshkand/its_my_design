# Generated by Django 2.1.1 on 2018-10-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(null=True),
        ),
    ]