from django.urls import path
from .views import BookAPIView
4
urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
]