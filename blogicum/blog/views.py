from django.shortcuts import render
from django.http import Http404


def index(request):
    """Отображает главную страницу"""
    template_name = "blog/index.html"
    return render(request, template_name, {"posts": reversed(posts)})


def post_detail(request, id):
    """Отображает конкретные посты"""
    template_name = "blog/detail.html"
    if id not in posts_collection:
        raise Http404("Страница не найдена!")
    post = posts_collection[id]
    return render(request, template_name, {"post": post})


def category_posts(request, category_slug):
    """Отображает список постов по категории"""
    template_name = "blog/category.html"
    return render(request, template_name, {"category_slug": category_slug})
