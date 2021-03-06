from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from book_store.models.book import Book, Transaction


class BookComment(TimeStampedModel):
    """책 디테일 페이지 댓글"""
    book_info = models.ForeignKey(Book)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='댓글 작성자')
    content = models.TextField('댓글 내용')


class TransactionComment(TimeStampedModel):
    """거래 포스트 댓글"""
    post = models.ForeignKey(Transaction)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='댓글 작성자')
    content = models.TextField('댓글 내용')