"""
1) добавим импорт вьюхи
2) добавим в список urlpatterns новое правило обработки адреса главной страницы

"""
from django.contrib import admin
from django.urls import path, include
from django_blog import views

urlpatterns = [
    path('', views.index),
    path('article/', include('django_blog.article.urls')),  # связать urlpatterns приложения с urlpatterns проекта
    path('admin/', admin.site.urls),
]

