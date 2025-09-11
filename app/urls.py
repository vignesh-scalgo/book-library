from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token 

from . import views

urlpatterns = [
    # path('booklist/', views.list_books, name="booklist"),
    path('booklist/', views.ListBooksView.as_view()),
    # path('authorlist/', views.list_author, name="authorlist"),
    path('authorlist/', views.ListAuthorView.as_view()),

    path('book/<int:id>/', views.SingleBookView.as_view()),
    path('book/', views.SingleBookView.as_view()), 
    path('author/<int:id>/', views.SingleAuthorView.as_view()),
    path('author/', views.SingleAuthorView.as_view()),
    path('booksbyauthor/<str:name>/', views.BooksByAuthorView.as_view()),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('token-auth-generate/', views.TokenGenerationView.as_view()),

    # Viewset based API's URLs (without router config)

    path('authorlist_viewset/', views.ListAuthorViewSetView.as_view({'get':'list'})),
    path('authorlist_viewset/<int:pk>/', views.ListAuthorViewSetView.as_view({'get':'retrieve'}))
]