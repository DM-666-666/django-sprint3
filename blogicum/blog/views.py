from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

NUMBER_OF_POSTS = 5


def index_filtration():
    """Производит фильтрацию постов"""
    return (
        Post.objects.select_related(
            "author",
            "location",
            "category"
        )
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
    )


def index(request):
    """Отображает главную страницу"""
    post_list = index_filtration()[:NUMBER_OF_POSTS]

    return render(request, "blog/index.html", {"post_list": post_list})


def post_detail(request, id):
    """Отображает конкретные посты"""
    post = get_object_or_404(index_filtration(), pk=id)

    return render(request, "blog/detail.html", {"post": post})


def category_posts(request, category_slug):
    """Отображает список постов по категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = index_filtration().filter(category=category)

    return render(
        request, "blog/category.html", {"category": category,
                                        "post_list": post_list}
    )
