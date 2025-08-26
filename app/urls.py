from django.urls import path

from . import views

urlpatterns = [
    # path('booklist/', views.list_books, name="booklist"),
    path('booklist/', views.ListBooksView.as_view(), name="booklist"),
    # path('authorlist/', views.list_author, name="authorlist"),
    path('authorlist/', views.ListAuthorView.as_view(), name="authorlist"),

    path('book/<int:id>/', views.SingleBookView.as_view(), name='book'),
    path('author/<int:id>/', views.SingleAuthorView.as_view(), name='author'),
    path('booksbyauthor/<str:name>/', views.BooksByAuthorView.as_view(), name='booksbyauthor'),
]