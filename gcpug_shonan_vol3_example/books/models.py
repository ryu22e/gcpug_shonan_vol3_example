"""書籍関連のモデル"""
from django.db import models


class Author(models.Model):
    """著者"""
    name = models.CharField(max_length=50, verbose_name="名前")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "著者"
        verbose_name_plural = "著者"


class Book(models.Model):
    """書籍"""
    title = models.CharField(max_length=100, verbose_name="タイトル")
    published_at = models.DateField(db_index=True, verbose_name="出版日")
    author = models.ForeignKey(Author, verbose_name="著者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "書籍"
        verbose_name_plural = "書籍"
        ordering = ('-published_at',)
