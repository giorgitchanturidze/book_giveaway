from books import views
from django.urls import path, include

urlpatterns = [
    path('books/', views.BooksList.as_view(), name="book_list"),
    path('books/<int:pk>', views.BookDetails.as_view(), name="book_details"),
    path('books/<int:pk>/request_book/', views.request_book, name="request_book")
]
