from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseForbidden
from project.views import trigger_404_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
]

urlpatterns += [
    re_path(r'^media/records/.*$', trigger_404_view),
    re_path(r'^media/photos/.*$', trigger_404_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
