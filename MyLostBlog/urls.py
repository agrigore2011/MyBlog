from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
path('admin/', admin.site.urls),
path('', include('Blog.urls', namespace='blog')),
#path('summernote/', include('django_summernote.urls')),
path('account/', include('account.urls')),
path('ckeditor/', include('ckeditor_uploader.urls')),
path('jet_api/', include('jet_django.urls')),
    ]

if settings.DEBUG:
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
