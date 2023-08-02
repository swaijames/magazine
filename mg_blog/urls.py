from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.news_detail, name='details'),
]
