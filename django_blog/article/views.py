from django.shortcuts import render


def index(request):
    app_name = 'DJANGO BLOG FOR DENISKA'  # Замените на реальное название вашего приложения
    return render(request, 'articles/index.html', {'app_name': app_name})
