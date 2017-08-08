from django.forms import ModelForm
from blog.models import Article
from blog.models import Comment

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text_content')

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('title', 'text_content')

