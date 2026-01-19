from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    # Link to the Book model.
    # related_name='reviews' allows you to access reviews via book.reviews.all()
    book = models.ForeignKey(
        'books.Book',
        #Cleanup crew: when a parent record - Book is deleted, the database automatically deletes all child records - Reviews
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    author = models.CharField(max_length=100)
    body = models.TextField()

    # Decimal (4,2) allows for ratings like 09.50 or 10.00
    # Added validators to ensure the rating stays within a logical range (e.g., 0-10)
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )

    # auto_now_add sets the timestamp only when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} for {self.book.title}"