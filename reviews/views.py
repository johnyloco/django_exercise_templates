from django.http import HttpResponse
from django.shortcuts import render


def reviews_list(request):
    return render(request, 'reviews/reviews.html')