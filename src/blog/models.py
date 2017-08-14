from django.db import models
from django.urls import reverse
# Create your models here.

from django.contrib.auth.models import User  # user model
from django.utils import timezone

from markdown_deux import markdown
from django.utils.safestring import mark_safe


class Article(models.Model):

    title = models.CharField(max_length=200)
    text_content = models.TextField(
        max_length=5000, help_text='enter a description')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True)

    def __str__(self):

        return self.title

    def get_detail_url(self):
        return reverse('article_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('article_update', args=[str(self.id)])

    def get_number_comments(self):
        return len(self.comment_set.all())

    def get_markdown(self):
        content = mark_safe(self.text_content)
        return markdown(content)

    def small_text(self):
        return self.get_markdown()[0: 600]
    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    author = models.ForeignKey(User, null=False)
    text_content = models.CharField(max_length=600)
    date = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, null=True)

    def __str__(self):
        return 'Comment: ' + self.text_content[:20]

    class Meta:
        ordering = ['-pk']
