from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:post_title>/', views.room, name='room'),
    # path('post-details/<id>/', views.post_details, name='post_details'),
]