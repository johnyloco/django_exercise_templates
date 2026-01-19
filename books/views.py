from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book


def books_list(request):
    all_books = Book.objects.all()
    return render(request, 'books/books.html', {'books': all_books})

def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)

    context = {"book": "book",
               "price": "price",
               "reviews": book.reviews.all()}

    return render(request, 'books/book_details.html', context = {'book': book})