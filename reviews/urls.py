from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.reviews_list, name='reviews'),
]