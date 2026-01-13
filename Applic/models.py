from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.title

class Borrow(models.Model):
    STATUS_CHOICES = [('Borrowed', 'Borrowed'), ('Returned', 'Returned')]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def __str__(self):
        return f"{self.member} - {self.book}"

class Fine(models.Model):
    borrow = models.OneToOneField(Borrow, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return f"Fine for {self.borrow}"
