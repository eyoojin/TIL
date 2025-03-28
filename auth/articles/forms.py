from django.forms import ModelForm
from .models import Article, Comment, Reply

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        # fields = '__all__'
        exclude = ('user', )

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content', )

class ReplyForm(ModelForm):
    class Meta():
        model = Reply
        fields = ('content', )