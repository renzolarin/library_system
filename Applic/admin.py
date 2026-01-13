from django.contrib import admin
from .models import Member, Author, Category, Book, Borrow, Fine

admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Fine)
