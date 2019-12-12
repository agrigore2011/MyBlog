from django.shortcuts import render, get_object_or_404
from .models import Post, Wisdom, Tag, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all()[:3]
    all_posts = Post.objects.all()

    wisdoms=Wisdom.objects.all()
    categorys=Post.objects.all()
    category = Category.objects.all()
    pop_posts = Post.objects.all()[:6]
    tags = Tag.objects.all()
    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:

        all_posts = paginator.page(1)
    except EmptyPage:

        all_posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html', {'page': page, 'posts': posts, 'all_posts':all_posts, 'wisdoms': wisdoms,
                   'pop_posts': pop_posts, 'categorys': categorys, 'category':category, 'tags':tags})


def post_detail(request, year,month,day,post):
    post=get_object_or_404(
        Post, slug=post,
        status='published',
        published__year=year,
        published__month=month,
        published__day=day,

    )
    return render(request, 'Blog/post/single-standard.html', {'post': post})

#filter idet po categoriyam? novosti otobrajaytsa?

def catdet(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    context = {
    'post': Post.objects.filter(category=category)
    }


    return render(request, 'Blog/category.html', context)

def tagdet(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    context = {
        'tags': Post.objects.filter(tag=tag)
    }


    return render(request, 'Blog/post/tag_detail.html', context)