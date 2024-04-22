"""
Здесь мы используем функцию render. Она формирует HTML на основе указанного шаблона
и использует при рендеринге  данные из словаря context.
"""

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World'
    })


def about(request):
    return render(request, 'abouth.html')
