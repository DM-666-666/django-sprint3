from django.shortcuts import render


def about(request):
    """Отображает страницу о проекте"""
    template_name = "pages/about.html"
    return render(request, template_name)


def rules(request):
    """Отображает страницу правил"""
    template_name = "pages/rules.html"
    return render(request, template_name)
