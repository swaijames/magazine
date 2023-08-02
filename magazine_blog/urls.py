from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mg_blog.admin import admin
from mg_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mg_blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
