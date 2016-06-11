"""書籍関連のビュー"""
from django.views.generic.list import ListView
from .models import Book


class ListView(ListView):
    """書籍一覧ビュー"""
    model = Book 
    queryset = Book.objects.select_related('author')
    template_name = 'list.html'
    paginate_by = 10
