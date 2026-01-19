from django.urls import path, include
from reviews import views

urlpatterns = [
    path('', include([
        path('', views.reviews_list, name='reviews'),
        path('<int:pk>/', views.review_details, name='review_details'),
    ])),
]