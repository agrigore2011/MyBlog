from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Post, Wisdom
from django.views.generic.list import ListView

from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all()
    a_posts = Post.objects.all()[:1]
    b_posts = Post.objects.all()[:1]
    c_posts = Post.objects.all()[:1]
    wisdoms=Wisdom.objects.all()
    categorys=Post.objects.all()

    pop_posts = Post.objects.all()[:6]

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html', {'page': page, 'posts': posts, 'wisdoms': wisdoms, 'a_posts': a_posts, 'b_posts': b_posts, 'c_posts': c_posts,
                   'pop_posts': pop_posts, 'categorys': categorys})




def post_detail(request, year,month,day,post):
    post=get_object_or_404(
        Post, slug=post,
        status='published',
        published__year=year,
        published__month=month,
        published__day=day,

    )
    return render(request, 'Blog/post/single-standard.html', {'post': post})


'''def tags_list(request):
    posts = Post.objects.filter(tag=tags_id)
    tags=Tag.object.all()
    current_tag=Tag.objects.get(pk=tags.id)
    context = {'posts': posts, 'tags': tags, 'current_tags': current_tags}
    return render(request, 'Blog//post/tags_list.html', context)

'''

