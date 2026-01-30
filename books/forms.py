from datetime import date

from django import forms

from books.models import Book


class BookFormBasic(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
    )

    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        min_value=0,
        label='Price (USD',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Price higher then 0'}),


    )

    isbn = forms.CharField(
        max_length=12,
        min_length=3,
    )

    genre = forms.ChoiceField(
        choices=Book.GenreChoices,
        widget=forms.RadioSelect
    )

    publishing_date = forms.DateField(
        initial=date.today(),
    )

    description = forms.CharField(
        widget=forms.Textarea()
    )

    img_url = forms.URLField(

    )

    publisher = forms.CharField(
        max_length=255,
    )