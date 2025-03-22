# modelForm

## 0. setting
- 가상환경 생성/ 활성화
- django 설치
- .gitignore 설정

## 1. Djnango
- startproject
- startapp/ 등록
```shell
django-admin startproject modelForm .
adjango-admim startapp articles
```
```python
# settings.py
INSTALLED_APPS = ['articles']
```

## 2. modeling/ migration
- modeling
```python
# models.py

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- migration
```shell
python manage.py makemigrations
python manage.py migrate
```
## 3. admin에 model 추가
```python
# admin.py
from .models import Article

admin.site.register(Article)
```

## 4. 공통 base.html 설정
- creatsuperuser
```shell
python manage.py creatsuperuser
```
- ../templates/'base.html'
```html
<!-- base.html -->
<h1>base</h1>
{% block body %}
{% endblock %}
```
```python
# settings.py
TEMPLATES = [{'DIR': [BASE_DIR / 'templates']}]
```

## 5. Read All 기능 구현
- url
```python
# ../'urls.py'
from django.urls import include

urlpatterns = [path('articles/', include('articles.urls'))]
```
- Read All
```python
# articles/'urls.py'
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [path('', view.index, name='index')]
```
```python
# views.py
from .models import Article

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)
```
```html
<!-- articles/templates/'index.html' -->
{% extends 'base.html' %}

{% block body %}
    {% for article in articles %}
        <h3>{{article.title}}</h3>
        <p>{{article.content}}</p>
    {% endfor %}
{% endblock %}
```

## 6. Create 기능 구현
- ModelForm
```python
# articles/'forms.py'
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
```

- Create
```python
# urls.py
path('create/', views.create, name='create')
```
- new/ 기능 구현
```python
# views.py
from .forms import ArticleForm

# new/ : 빈 종이를 보여주는 기능 => GET create/
# create/ : 사용자가 입력한 데이터 저장 => POST create/

def create(request):
    if request.method == 'POST': # create/
        pass
    else: # new/
        form = ArticleForm()

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)
        
```
```html
<!-- creat.html -->
{% extends 'base.html' %}

{% block body %}
<!-- action을 비워두면 현재 위치로 요청을 보냄 -->
<form action="" method=POST>
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>
{% endblock %}
```
- create/ 기능 구현
```python
# views.py
from django.shortcuts import redirect
    if request.metho == 'POST':
        form = ArticleForm(request.POST)
        # request.POST: dictionary
        # 내가 만든 폼에 사용자가 입력한 데이터를 넣어줌

        if form.is_valid():
        # 폼에 있는 데이터가 유효한가요?
            form.save()
            return redirect('articles.index')
        else:
        # 유효하지 않으면 먼저 작성해둔 건 그대로 두고 다시 작성하도록 요구
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)
```
- Create 흐름 이해하기
```python
# 모든 경우의 수
# GET: form을 만들어서 html 문서를 사용자에게 리턴
# POST: invalid data (데이터 검증 실패)
# POST: valid data (데이터 검증 성공)

def creat(request):

    # 5. POST 요청 (invalid data)
    # 10. POST 요청 (valid data)
    if request.method == 'POST':
        
        # 6. 사용자가 입력한 데이터(request.POST)를 담은 form 생성 (invalid)
        # 11. 사용자가 입력한 데이터(request.POST)를 담은 form 생성 (valid)
        form = ArticleForm(request.POST)

        # 7. form을 검증 -> 실패
        # 12. form을 검증 -> 성공
        if form.is_valid():
            
            # 13. form 저장
            form.save()

            # index로 redirect
            return redirect('articles:index')
    
    # 1. GET 요청
    else:

        # 2. 비어있는 form을 만든다
        form = ArticleForm()

    # 3. context dict에 비어있는 form을 담는다
    # 8. context dict에 실패한 form을 담는다
    context = {
        'form': form,
    }

    # 4. create.html을 렌더링
    # 9. create.html을 렌더링 
    return render(request, 'creat.html', context)
```