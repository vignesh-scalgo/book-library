from django.shortcuts import render

from .models import Author, Books

from .serializers import AuthorSerializer, BooksSerializer

from rest_framework.response import Response

# Function based view

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated

# Class based view

from rest_framework.views import APIView

from rest_framework import status


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

    # API logic to Read Author

    def get(self,request,*args,**kwargs):

        id = kwargs.get('id')

        query = Author.objects.filter(author_id = id)

        serializer_class = AuthorSerializer(query, many= True)

        return Response(serializer_class.data)
    
    # API logic to Create Author

    def post(self,request,*args,**kwargs):

        record_to_create = request.data

        serializer_obj = AuthorSerializer(data = record_to_create)

        if serializer_obj.is_valid(raise_exception = True):

            serializer_obj.save()

            return Response(serializer_obj.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer_obj.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # API logic to Update Author

    def put(self,request,*args,**kwargs):

        id = kwargs.get('id')

        query = Author.objects.get(author_id = id)

        record_to_update = request.data

        serializer_obj = AuthorSerializer(query,data = record_to_update)

        if serializer_obj.is_valid(raise_exception = True):

            serializer_obj.save()

            return Response(serializer_obj.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # API logic to Delete Author

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        author_record = Author.objects.get(author_id = id)

        author_record.delete()

        return Response(status=status.HTTP_200_OK)

    
#Book API View

class SingleBookView(APIView):

    # API to view book

    def get(self,reuest,*args,**kwargs):

        id = kwargs.get('id')

        query = Books.objects.filter(book_id = id)

        serializer_class = BooksSerializer(query, many=True)

        return Response(serializer_class.data)
    
    # API to create book

    def post(self,request,*args,**kwargs):

        new_record = request.data

        author_name = new_record.get('book_author')

        author_record = Author.objects.get(author_name = author_name)

        author_id = author_record.author_id

        new_record.update({'book_author':author_id})

        serializer_obj = BooksSerializer(data = new_record)

        if serializer_obj.is_valid(raise_exception=True):

            serializer_obj.save()

            return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    # API to update book

    def put(self,request,*args,**kwargs):

        id = kwargs.get('id')

        query = Books.objects.get(book_id = id)

        record_to_update = request.data

        author_name = record_to_update.get('book_author')

        author_record = Author.objects.get(author_name = author_name)

        author_id = author_record.author_id

        record_to_update.update({'book_author':author_id})

        serializer_obj = BooksSerializer(query, data = record_to_update)

        if serializer_obj.is_valid(raise_exception=True):

            serializer_obj.save()

            return Response(serializer_obj.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # API to delete book

    def delete(self,request,*args,**kwargs):

        id = kwargs.get('id')

        book_record = Books.objects.get(book_id = id)

        book_record.delete()

        return Response({'success':'record deleted successfully'},status=status.HTTP_200_OK)

    
# API View to filter out all the books based on author name
    
class BooksByAuthorView(APIView):

    def get(self, request, *args, **kwargs):

        author_name = kwargs.get('name')

        query = Books.objects.filter(book_author__author_name = author_name)

        serializer_class = BooksSerializer(query, many=True)

        return Response(serializer_class.data)