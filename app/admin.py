from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin

from .models import Books, Author

# admin.site.register(Books)
# admin.site.register(Author)

@admin.register(Books)
class BooksAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    # search_fields = ['book_name', 'book_author', 'book_categorey']
    pass


@admin.register(Author)
class AuthorAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    # search_fields = []
    pass