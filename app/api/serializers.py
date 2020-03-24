from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Author, Book, Basket


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Book
        fields = ['url', 'type', 'title', 'isbn', 'price', 'discount', 'authors']


class BasketSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False, read_only=True)

    class Meta:
        model = Basket
        fields = ['url', 'books', 'total']
