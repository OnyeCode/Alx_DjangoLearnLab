from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # ALX expects:
    # "books/update"
    # "books/delete"
    # so the pk must come AFTER the keyword
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),

    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
]

