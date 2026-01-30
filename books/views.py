from django.contrib.admin.templatetags.admin_list import search_form
from django.db.models import Avg, Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookFormBasic, BookEditForm, BookDeleteForm, BookSearchForm
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
    search_form = BookSearchForm(request.GET or None)

    all_books = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    )

    if 'query' in request.GET:
        if search_form.is_valid():
            search_value = search_form.cleaned_data['query']
            all_books = all_books.filter(
                Q(title__icontains=search_value)
                |
                Q(description__icontains=search_value)
            )


    context = {
        'books': all_books,
        'page_title': 'Books List',
        'search_form': search_form,
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
        form.save()
        return redirect ('books:home')

    context = {
        "form" : form,

    }

    return render(request, 'books/book_create.html', context)


def book_edit(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect ('books:book_details', book.slug)

    context = {
        "form" : form,

    }

    return render(request, 'books/book_edit.html', context)


def book_delete(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect ('books:books_list')

    context = {
        "form" : form,

    }

    return render(request, 'books/book_delete.html', context)