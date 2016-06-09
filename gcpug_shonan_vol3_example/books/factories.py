"""書籍関連のファクトリークラス"""
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory
from .models import Author, Book
import datetime


class AuthorFactory(DjangoModelFactory):
    """books.models.Author のファクトリークラス"""
    name = factory.Faker('name', locale='ja_JP')

    class Meta:
        model = Author
        django_get_or_create = ('name',)


class BookFactory(DjangoModelFactory):
    """books.models.Book のファクトリークラス"""
    title = factory.Sequence(lambda n: '書籍タイトル{}'.format(n + 1))
    author = factory.SubFactory(AuthorFactory)
    published_at = fuzzy.FuzzyDate(
        datetime.date(1990, 1, 1),
        datetime.date(2016, 1, 1)
    )
    class Meta:
        model = Book
