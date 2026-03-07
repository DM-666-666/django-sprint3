from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone

from .models import Post, Category


def index(request):

    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-created_at')[:5]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):

    post = get_object_or_404(Post, pk=id)
    if (
        post.pub_date > timezone.now()
        or not post.is_published
        or not post.category.is_published
    ):
        raise Http404("Публикация не найдена или недоступна")

    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404("Категория не опубликована")

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    return render(request, 'blog/category.html', {'category': category,
                                                  'post_list': post_list})
