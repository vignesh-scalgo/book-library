from django.urls import path

from . import views

urlpatterns = [
    # path('booklist/', views.list_books, name="booklist"),
    path('booklist/', views.ListBooksView.as_view()),
    # path('authorlist/', views.list_author, name="authorlist"),
    path('authorlist/', views.ListAuthorView.as_view()),

    path('book/<int:id>/', views.SingleBookView.as_view()),
    path('book/', views.SingleBookView.as_view()),
    path('author/<int:id>/', views.SingleAuthorView.as_view()),
    path('booksbyauthor/<str:name>/', views.BooksByAuthorView.as_view()),
]