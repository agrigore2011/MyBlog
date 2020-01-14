from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import Post, Wisdom, Tag, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm


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
    return render(request,'Blog/post/list.html', {'page': page, 'posts': posts, 'all_posts':all_posts, 'wisdoms': wisdoms,
                   'pop_posts': pop_posts, 'categorys': categorys, 'category':category, 'tags':tags})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   published__year=year,
                                   published__month=month,
                                   published__day=day)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'Blog/post/single-standard.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})




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



def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'Blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})

def about (request):
    return render(request, 'Blog/about.html')