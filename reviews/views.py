from django.http import HttpResponse
from django.shortcuts import render

from reviews.models import Review


def reviews_list(request):
    all_reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html',{'reviews': all_reviews})

def review_details(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'reviews/reviews_details.html', {'review': review})