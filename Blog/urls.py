from django.urls import path
from .views import post_list, post_detail, catdet, tagdet,post_share

app_name = 'Blog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail, name='post_detail'),
    path('category/<str:slug>', catdet, name='catdet'),
    path('tag/<str:slug>', tagdet, name='tagdet'),
    path('<int:post_id>/share/',post_share, name='post_share'),



]