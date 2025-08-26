from django.db import models

# Author model

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=25)
    author_language = models.CharField(max_length=20)
    author_age = models.IntegerField()
    author_nationality = models.CharField(max_length=15)

    class Meta:

        ordering = ['author_id']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.author_name}'

# Books model

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=45)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_categorey = models.CharField(max_length=20)
    book_price = models.IntegerField()

    class Meta:

        ordering = ['book_id']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.book_id} {self.book_name} {self.book_author}'