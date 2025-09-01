# Book Project

### Features:

    1. A Django project.
    2. Connected the newly created project to a MySQL database. 
    3. Created 2 models named Author and Book
    4. Book have a Foreign key relationship to the Author. (One Author can write 1 or more books.)
    5. Registered the 2 models on Django Admin
    6. Added search functionality on Django admin
    7. Created APIs for
        1. To Create an author
        2. To Create books with link to author
        3. To List all books
        4. To Fetch all books by a given author.
        5. To Update books
        6. To Update authors
        7. To Delete Book
        8. To Delete Author

    
    ** Installed Django resframework for the APIs
    ** Used virtualenv for the project (With the help 'pyenv')

###### Dependencies:

    Refer: requirement.txt 

###### Secretkey and Database credentials:

    Protected by .env file (ignored by .gitignore) with the help of python decouple

## Models:

#### 1. Author Model

    Fields:

        author_id
        author_name
        author_language 
        author_age
        author_nationality

#### 2. Books Model

    Fields:

        book_id
        book_name 
        book_author -> (Author Name) Foreign key relationship to the Author
        book_categorey 
        book_price 

## Django Admin:

    - Registered the 2 models on Django Admin
    - Implemented search functionality by 'DjangoQLSearchMixin'

## Serializers:

    - Two model based serializers created with respect to models with all fields
        1. AuthorSerializer
        2. BooksSerializer  -> defined function 'to_representation': to representation 'author_name' instead of 'author_id'

## Urls and Views:

    Views -> Class based views, implemented by inheriting 'APIView'

    1. To display all authors,

        Url: authorlist/
        View: ListAuthorView (methods: GET)

    2. To display all books,

        Url: booklist/
        View: ListBooksView (methods: GET)

    3. CRUD operation in author

        Url: author/<int:id>/
        View: SingleAuthorView (methods: GET, PUT, DELETE)

        :to create author
            Url: author/    (New url to handle <int:id>)
            View: SingleAuthorView (methods: POST)

    4. CRUD operation in book

        Url: book/<int:id>/
        View: SingleBookView (methods: GET, PUT, DELETE)

        :to create book     (New url to handle <int:id>)
            Url: book/
            View: SinglebookView (methods: POST)

    5. API View to filter out all the books based on author name

        Url: booksbyauthor/<str:name>/
        View: BooksByAuthorView (methods: GET)

## Authentication:

#### Implemented Basic Authentication

    - With the help of Super User's username and password

#### Implemented Token Authentication

    - Created Super User
    - Generated and Assignesd token to the Super User using the below command,
        cmd: python manage.py drf_create_token <username>
    - Authenicated by Token <Token Id> with the help of postman

#### Implemanted Custom Authentication

    - Hard coded credentials (username and password) in 'settings.py'
    - Sent request with new credentials (hard coded credentials)
    - Logics in 'app/authentication.py'
        - Inherited 'BaseAuthentication' 'from rest_framework/authentication' module
        - Fetched token from request.headers
        - Decrypted token - found username and password
        - Checked this credentials with hard coded credentials
        - Username is registered in Users db table with the help of 'get_or_create' method
        - Finally, granted access


### <!-- The End -->