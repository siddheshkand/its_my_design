from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from its_my_design import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^imagefit/', include('imagefit.urls')),
    url(r'^', include('Home.urls')),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
