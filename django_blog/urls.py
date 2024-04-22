"""
1) добавим импорт вьюхи
2) добавим в список urlpatterns новое правило обработки адреса главной страницы

"""
from django.contrib import admin
from django.urls import path
from django_blog import views

urlpatterns = [
    path('', views.index),
    path('abouth/', views.about),
    path('admin/', admin.site.urls),
]

