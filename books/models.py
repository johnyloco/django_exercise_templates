from django.db import models
from django.template.defaultfilters import slugify

from common.models import TimeStampModel


class Book(TimeStampModel):

    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction', 'Fiction'
        NON_FICTION = 'Non-Fiction', 'Non-Fiction'
        FANTASY = 'Fantasy', 'Fantasy'
        SCIENCE = 'Science', 'Science'
        HISTORY = 'History', 'History'
        MYSTERY = 'Mystery', 'Mystery'


    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Fixed length (12) is enforced via max_length;
    # Logic for exact length can be added via a Validator.
    isbn = models.CharField(max_length=12, unique=True)

    genre = models.CharField(
        max_length=50,
        choices=GenreChoices.choices,
    )

    description = models.TextField()
    image_url = models.URLField()
    publisher = models.CharField(max_length=255)


    # Slug is unique and generated from the title
    slug = models.SlugField(max_length=255, unique=True, blank=True,)

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        null=True,
    )


    def save(self, *args, **kwargs) -> None:
        # Automatically generate slug if it doesn't exist
        if not self.slug and self.title:
            self.slug = slugify(f"{self.title}-{self.publisher}")
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        max_length=50
    )
    books = models.ManyToManyField(
        Book,
    )

    def __str__(self) -> str:
        return self.name