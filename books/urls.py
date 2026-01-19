from django.urls import path, include

from books import views

from django.urls import path, include
from . import views

# Grouped under the 'books/' prefix
urlpatterns = [
    path('', include([
        path('', views.books_list, name='books_list'),
        path('<slug:slug>/', views.book_details, name='book_details'),
    ])),
]