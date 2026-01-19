from django.urls import path, include

from books import views

urlpatterns = [
    path('', views.books_list, name='books'),
]