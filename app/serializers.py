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

    class Meta:

        model = Books

        fields = '__all__'

    # Code to return 'author_name' instead of 'author_id'

    def to_representation(self, instance):

        data = super().to_representation(instance)

        data['book_author'] = instance.book_author.author_name

        # data['book_categorey'] = instance.book_author.author_language

        return data
    
"""
# Token based authentication - by default user model

# Serializer for credentials to generate token
# Simple serializer

class CredentialsSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        
        user_name = data.get('username')
        pass_word = data.get('password')

        if user_name and pass_word:

            user = authenticate(username = user_name, password = pass_word)

            if user is None:
                
                raise serializers.ValidationError("Invalid credentials")
            
            data['user'] = user

            return data
        
        else:
            
            raise serializers.ValidationError("Both username and password are required")
        

# Serializer for user_auth Model
# To return usre details with token

users = get_user_model()

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = users

        fields = '__all__'
"""