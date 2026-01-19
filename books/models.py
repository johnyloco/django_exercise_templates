from django.db import models
from django.template.defaultfilters import slugify


class Book(models.Model):
    # Choices for the genre field
    objects = None
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-Fiction'),
        ('FANTASY', 'Fantasy'),
        ('SCIENCE', 'Science'),
        # Add more genres as needed
    ]

    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Fixed length (12) is enforced via max_length;
    # Logic for exact length can be added via a Validator.
    isbn = models.CharField(max_length=12, unique=True)

    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()

    # Slug is unique and generated from the title
    slug = models.SlugField(max_length=255, unique=True, blank=True,)

    # auto_now updates the field every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically generate slug if it doesn't exist
        if not self.slug and self.title:
            self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title