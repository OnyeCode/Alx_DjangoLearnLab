from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
        path('books/', BookListView.as_view(), name='BookList'),
        path('books/<int:pk>/', BookDetailView.as_view(), name='BookDetail'),
        path('books/create/', BookCreateView.as_view(), name='BookCreate'),
        path('books/update/', BookUpdateView.as_view(), name='BookUpdate'),
        path('books/delete/', BookDeleteView.as_view(), name='BookDelete'),
        ]
