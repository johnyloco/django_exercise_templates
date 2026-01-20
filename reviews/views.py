from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from reviews.models import Review


def reviews_list(request: HttpRequest) -> HttpResponse:
    all_reviews = Review.objects.all()
    return render(request, 'reviews/reviews.html',{'reviews': all_reviews})

def review_details(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk,
    )

    context = {
        'review': review,
        'page_title': f'Review {review.author}\'s review on {review.book.title}'
    }
    return render(request, 'reviews/reviews_details.html', context)