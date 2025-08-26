from django.shortcuts import render

from .models import Author, Books

from .serializers import AuthorSerializer, BooksSerializer

from rest_framework.response import Response

# Function based view

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated

# Class based view

from rest_framework.views import APIView


# Function based view

"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])      # To verify user is logined
def list_books(request):

    # ORM query to fetch all book's records
    query = Books.objects.all()

    # Code to serialize fetched data
    serializer_class = BooksSerializer(query, many=True)

    return Response(serializer_class.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_author(request):

    query = Author.objects.all()

    serializer_class = AuthorSerializer(query, many=True)

    return Response(serializer_class.data)
"""

# Class based views

# Author API View

class ListAuthorView(APIView):

    def get(self,request,*args,**kwargs):

        # ORM query to fetch all book's records

        query = Author.objects.all()

        # Code to serialize fetched data

        serializer_class = AuthorSerializer(query, many= True)

        return Response(serializer_class.data)
    
# Books API View

class ListBooksView(APIView):

    def get(self,request,*args,**kwargs):

        query = Books.objects.all()

        serializer_class = BooksSerializer(query, many=True)

        return Response(serializer_class.data)

# Individual Author and Book API view

#Author API View

class SingleAuthorView(APIView):

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        query = Author.objects.filter(author_id = id)

        serializer_class = AuthorSerializer(query, many= True)

        return Response(serializer_class.data)
    
#Book API View

class SingleBookView(APIView):

    def get(self,reuest,*args,**kwargs):

        id = kwargs.get('id')

        query = Books.objects.filter(book_id = id)

        serializer_class = BooksSerializer(query, many=True)

        return Response(serializer_class.data)
    
# API View to filter out all the books based on author name.
    
class BooksByAuthorView(APIView):

    def get(self, request, *args, **kwargs):

        author_name = kwargs.get('name')

        query = Books.objects.filter(book_author__author_name = author_name)

        serializer_class = BooksSerializer(query, many=True)

        return Response(serializer_class.data)