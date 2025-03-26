# 1:N
- 댓글은 게시물에 속해 있음
- DB에서는 하나의 셀에 하나의 데이터만 저장함
- 데이터베이스 정규화(목적: 데이터를 쪼개고 중복을 피함)
- 게시글과 댓글을 분리

## 0. .gitignore 설정
- 가상환경 생성/ 활성화
- .gitignore 설정
- django 설치

## 1. project, app 생성 및 등록

## 2. 공통 html 구조 작성

## 3. Article modeling, migration

## 4. Article Create
- ModelForm(ArticleForm) 생성
```python
# articles/'forms.py'
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
```
```python
# views.py
from django.shortcuts import redirect
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        form = ArticocleForm(request.POST) # 사용자의 정보를 담은
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm() # 비어있는
    
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)
```
```html
<!-- articles/templates/'create.html' -->
<form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>
```

## 5. Article Read

## 6. Article Update
```python
# views.py
from .models import Article

def update(requst, id):
    article = Article.objects.get(id=id) # 이전에 있던 정보

    if request.method == 'POST':
        # article = Article.objects.get(id=id) # 이전에 있던 정보
        form = ArticleForm(request.POST, instance=article)
        # (새로운 정보, 기존 정보)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    else:
        # article = Article.objects.get(id=id) # 이전에 있던 정보

        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)
```
```html
<!-- update.html -->
<form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>    
```

## 7. Article Delete

## 8. Comment modeling, migration
- modeling
```python
# models.py
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # on_delete: 게시글이 지워졌을 때, CASCADE: 댓글을 전부 지움
```
- migration
```shell
python manage.py makemigrations
python manage.py migrate
```

## 9. Comment Create
- ModelForm(CommentForm) 생성
```python
# forms.py
from .models import Comment

class CommentForm(ModelForm):
    class Meta():
        model = Comment

        # 둘 중에 하나 선택
        fields = ('content', ) # 추가할 필드 목록
        exclude = ('article', ) # 제외할 필드 목록
```
- GET 요청
```python
# views.py
from .forms import CommentForm

def detail(request, id):
    form = CommentForm()

    context = {
        'form': form,
    }
```
```html
<!-- detail.html -->
<form action="{% url 'articles:comment_create' article_id %}" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>
```
- POST 요청
```python
# views.py
def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # commit: 데이터베이스에 완전히 저장 -> False: 임시 저장
            # comment의 article_id 값이 비어있으므로 먼저 찾아야 함
            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('articles:detail', id=article_id)
    else:
        return redirect('articles:index')
```

## 10. Comment Read
```python
# models.py
class Article(models.Model):
    # comment_set => article을 이용해 comment에 접근

class Comment(models.Model):
    # article_id => comment를 이용해 article에 접근
    # DB에는 article 객체를 저장할 필요 없기 때문에 article_id가 저장됨
```
- 아래 두개 html 중에 선택
```html
<!-- detail.html -->
 {% for comment in article.comment_set.all %}
    <li>{{comment.content}}</li>
 {% endfor %}
```
```python
# views.py
def detail(request, id):
    comments = article.comment_set.all()

    context = {
        'comments': comments,
    }
```
```html
<!-- detail.html -->
{% for comment in comments %}
    <li>{{comment.content}}</li>
{% endfor %}
```

## 11. Comment Delete
```python
# urls.py
path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name='comment_delete')
```
```python
# views.py
from .models import Comment

def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('articles:detail', id=article_id)
```

## 12. Create CSS
```python
# forms.py
from django import forms

class ArticleForm(ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta():
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
```