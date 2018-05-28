from django.contrib import admin

# Register your models here.
from Home.models import Category, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'media', 'media_type', 'youtube_url'
    )
    # list_editable = (
    #     'youtube_url',
    # )
    #
    # name = models.CharField(max_length=100)
    # description = models.CharField(max_length=500, blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # media = models.FileField(upload_to=project_media_path)
    # media_type = models.BooleanField(default=0)
    # youtube_url = models.URLField(default="")


admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
