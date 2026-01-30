from datetime import date
from typing import Any

from django import forms

from books.models import Book, Tag


# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title'}),
#     )
#
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
#         label='Price (USD',
#         widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Price higher then 0'}),
#
#
#     )
#
#     isbn = forms.CharField(
#         max_length=12,
#         min_length=3,
#     )
#
#     genre = forms.ChoiceField(
#         choices=Book.GenreChoices,
#         widget=forms.RadioSelect
#     )
#
#     created_at = forms.DateField(
#         initial=date.today(),
#     )
#
#     description = forms.CharField(
#         widget=forms.Textarea()
#     )
#
#     image_url = forms.URLField()
#
#     publisher = forms.CharField()


class BookFormBasic(forms.ModelForm):
    tags = forms.CheckboxSelectMultiple()

    # order of fields in the form
    field_order = [
        'title',
        'price',
    ]

    class Meta:
        model = Book
        exclude = ('slug',)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()


class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(BookFormBasic):
    # class Meta(BookFormBasic.Meta):
    #     widgets = {
    #         'title': forms.TextInput(attrs={'disabled': True}),
    #     }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled= True

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False, # it can be empty
    )

