from django.http import HttpResponse
from django.shortcuts import render


def books_list(request):
    return render(request, 'books/books.html')