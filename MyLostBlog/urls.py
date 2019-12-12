from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Blog.views import about




urlpatterns = [
path('admin/', admin.site.urls),
path('', include('Blog.urls', namespace='blog')),
path ('about/', about, name='about'),
path('summernote/', include('django_summernote.urls')),
path('account/', include('account.urls')),
    ]

if settings.DEBUG:
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)