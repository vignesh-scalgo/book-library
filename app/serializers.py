from .models import Author, Books

from rest_framework import serializers

# import for token based authentication by default user model

from django.contrib.auth import get_user_model, authenticate



# Model based serializer

#Serializer for Author model

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author

        fields = '__all__'

#Serializer for Books Model

class BooksSerializer(serializers.ModelSerializer):

    # to add one more extra field in book response
    # author_age from author model
    # get_author_age()

    author_age = serializers.SerializerMethodField()

    class Meta:

        model = Books

        # fields = '__all__'

        fields = [
            'book_id',
            'book_name',
            'book_categorey',
            'book_price',
            'book_author',
            'author_age'
        ]

    # Code to return 'author_name' instead of 'author_id'

    def to_representation(self, instance):

        data = super().to_representation(instance)

        data['book_author'] = instance.book_author.author_name

        # data['book_categorey'] = instance.book_author.author_language

        return data
    
    def get_author_age(self,instance):

        try:
            author_age = instance.book_author.author_age
            return author_age
        except:
            return None