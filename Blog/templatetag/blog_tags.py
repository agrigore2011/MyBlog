from django import template
from ..models import Post



register = template.Library()
@register.simple_tag(name='blog_tags')
def total_posts():
    return Post.published.count()


register = template.Library()
@register.inclusion_tag('blog/post/tags_list.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-published')[:count]
    return {'latest_posts': latest_posts}
