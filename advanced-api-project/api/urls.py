from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
        path('', BookListView.as_view(), name='BookList'),
        path('<int:pk>/', BookDetailView.as_view(), name='BookDetail'),
        path('create/', BookCreateView.as_view(), name='BookCreate'),
        path('update/', BookUpdateView.as_view(), name='BookUpdate'),
        path('delete/', BookDeleteView.as_view(), name='BookDelete'),
        ]
