# relationship_app/urls.py
from django.urls import path
from .views import (
    author_list, author_create,
    author_edit, author_delete
)

urlpatterns = [
    path('authors/', author_list, name='author_list'),
    path('authors/create/', author_create, name='author_create'),
    path('authors/<int:pk>/edit/', author_edit, name='author_edit'),
    path('authors/<int:pk>/delete/', author_delete, name='author_delete'),
]
