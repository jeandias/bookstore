from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    TYPE_EXCLUSIVE = 'Exclusive'
    TYPE_NEW = 'New'
    TYPE_USED = 'Used'

    TYPE_CHOICES = (
        (TYPE_EXCLUSIVE, 'Exclusive'),
        (TYPE_NEW, 'New'),
        (TYPE_USED, 'Used'),
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )
    title = models.CharField(max_length=100, null=False)
    isbn = models.CharField(max_length=20, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return f"{'€{:7,.2f}'.format(self.price)} [{self.type}] {self.title} - {self.list_authors}"

    @property
    def list_authors(self):
        return ", ".join(map(lambda a: a.name, self.authors.all()))

    @property
    def discount(self):
        switcher = {
            'Exclusive': self.price,
            'New': self.price - self.price * 10 / 100,
            'Used': self.price - self.price * 25 / 100
        }
        return switcher.get(self.type, "Invalid type")


class Basket(models.Model):
    books = models.ManyToManyField(Book, related_name='baskets')

    @property
    def total(self):
        return sum(map(lambda b: float(b.discount), self.books.all()))
