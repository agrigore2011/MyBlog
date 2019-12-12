from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Blog.views import about



urlpatterns = [
path('admin/', admin.site.urls),
path('blog/', include('Blog.urls', namespace='blog')),
path('summernote/', include('django_summernote.urls')),
path('accounts/', include('account.urls')),
path('about/', about, name='about'),

]

if settings.DEBUG:
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)