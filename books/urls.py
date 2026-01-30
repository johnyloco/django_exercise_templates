from django.urls import path, include

from books import views



app_name = 'books'

book_patterns = [
    path('', views.books_list, name='books_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/', include([
        path('edit/', views.book_edit, name='book_edit'),
        path('delete/', views.book_delete, name='book_delete'),
         ])),
    path('<slug:slug>/', views.book_details, name='book_details'),

]

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', include(book_patterns)),
]
