"""書籍関連のテスト"""
from django.test import TestCase
from django.core.urlresolvers import reverse
from .factories import BookFactory


class ListViewTests(TestCase):
    """書籍一覧ビューのテスト"""

    def setUp(self):
        """前準備"""
        self.title = 'テストタイトル'
        self.books = BookFactory.create_batch(20, title=self.title)

    def test_show_page(self):
        """書籍一覧を表示できる"""
        r = self.client.get(reverse('books:list'))
        self.assertContains(r, self.title, count=10, status_code=200)
