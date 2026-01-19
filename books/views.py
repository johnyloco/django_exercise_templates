from django.http import HttpResponse
from django.shortcuts import render

def books_list(request):
    return HttpResponse("books list")