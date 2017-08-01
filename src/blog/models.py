from django.db import models

# Create your models here.


class Tag(models.Model):

    word = models.CharField(max_length=50)

    def __str__(self):

        return self.word


class Article(models.Model):

    title = models.CharField(max_length=200)
    text_content = models.TextField(
        max_length=5000, help_text='enter a description')
    tags = models.ManyToManyField(Tag)
    date = models.DateField()

    def __str__(self):

        return self.title

    def small_text(self):

        return self.text_content[0: 600] + ' ...'
