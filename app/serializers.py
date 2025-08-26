from .models import Author, Books

from rest_framework import serializers

# Model based serializer

#Serializer for Author model

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Author

        fields = '__all__'

#Serializer for Books Model

class BooksSerializer(serializers.ModelSerializer):

    class Meta:

        model = Books

        fields = '__all__'

    # Code to return 'author_name' instead of 'author_id'

    def to_representation(self, instance):

        data = super().to_representation(instance)

        data['book_author'] = instance.book_author.author_name

        # data['book_categorey'] = instance.book_author.author_language

        return data