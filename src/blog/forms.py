from django import forms
from blog.models import Article
from blog.models import Comment
# Виджет с разметкой 


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text_content')

class CommentForm(forms.ModelForm):
	text_content = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = Comment
		fields = ('text_content', )

