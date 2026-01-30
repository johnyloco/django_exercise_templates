from django.db.models import Avg
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic
from books.models import Book

def home(request: HttpRequest) -> HttpResponse:
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-created_at').first()

    context = {
        'total_books': total_books,
        'latest_book': latest_book,
        'page_title': 'Home',
    }
    return render(request, 'books/home.html', context)


def books_list(request: HttpRequest) -> HttpResponse:
    all_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    )

    context = {
        'books': all_books,
        'page_title': 'Books List',
    }
    return render(request, 'books/books.html', context)

def book_details(request: HttpRequest, slug: str) -> HttpResponse:
    book = get_object_or_404(Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ),
        slug=slug,
    )

    context = {"book": book,
               "page_title": 'Book Details',
               }

    return render(request, 'books/book_details.html', context)

def book_create(request: HttpRequest) -> HttpResponse:
    form = BookFormBasic(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        return redirect ('books:home')

    context = {
        "form" : form,

    }

    return render(request, 'books/book_create.html', context)