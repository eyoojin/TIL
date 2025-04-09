# auth

- 로그인 관련 기능
    - authentication >> 인증
    - authorization
- 프로젝트를 만들 때
    - 데이터베이스의 **구조 설계**를 먼저 하는 것이 좋음
        - 무슨 데이터를 저장하고 싶은지
        - 데이터끼리 어떤 상관관께를 가지는지
- 오늘 프로젝트의 구조
    - User -< Post
    - User -< Comment
    - Post -< Comment

## 0. .gitignore 설정

- 가상환경 생성/활성화
- django 설치
- .gitignore 설정

## 1. startproject

```shell
django-admin startproject auth .
```

## 2. startapp accounts

```shell
django-admin startapp accounts
```
- settings.py에 앱 등록

## 3. base.html

- settings.py에 등록

# 회원가입/로그인/로그아웃

## 4. User modeling/migration

- modeling
```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```
- Django는 원래 사용하던 User 모델이 있기 때문에 내가 새로 만든 것과 충돌이 날 수 있음 -> Django에게 내가 만든 모델로 사용하겠다고 알려줘야 함
```python
# auth/settings.py
AUTH_USER_MODEL = 'accounts.User'
```

## 5. Signup - Create

- 경로 설정: auth -> accounts
- Form
```python
# accounts/forms.py
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', )
        # password는 필수
```
```html
<!-- accounts/templates/signup.html -->
<form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>
```
```python
# accounts/views.py
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
```
- validaion check (유효성 검사)
    - `if form.is_valid()`에서 처리
    - 비밀번호가 너무 짧거나 흔하거나 등등
---
- 암호화
    - 평문을 난수로 바꿈
    - hash 함수
        - 어떠한 계산의 결과
        - sha1: 결과를 보고 원본을 유추 가능
        - sha256: 현재 쓰는 암호화 함수
    - salt
        - 사람마다 다른 랜덤한 문자열을 추가로 붙임 -> 똑같은 비밀번호도 다르게 저장됨

## 6. Login - Create

1. User가 ID와 PW를 server로 보냄
2. ID/PW가 가지고 있는 데이터와 일치하는지 확인
3. User Session(임의의 난수) 키 발급 -> **Create**
4. Session을 cookies에 저장

- 쿠키를 허용함: 브라우저의 일정 공간에 데이터를 저장하도록 허용함
---
- 경로 설정
- Form
```python
# accounts/forms.py
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    pass
```
```html
<!-- accounts/templates/login.html -->
<form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">
</form>
```
```python
# accounts/views.py
from .forms import CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# 장고가 이미 만들어둔 로그인 함수
# 우리가 만든 함수와 이름이 같아서 충돌이 일어날 수 있으므로 이름 변경

def login(request):
    if request.method == 'POST':
        form = CustomAuthentication(request, request.POST)
        # request.POST: ID, PW 정보가 담긴
        if form.is_valid():
            auth_login(request, form.get_user())
            # form.get_user(): 실제 유저 데이터(ID)
            # auth_login: 세선 발급해주는 함수
            return redirect('articles:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)
```
- navbar
```html
<!-- ../templates/base.html -->
<nav class="nav">
    <!-- {{user}}: context에 담지 않아도 이미 가지고 있는 변수 -->
    <a href="" class="nav-link disabled">{{user}}</a>
    <a href="{% url 'accounts:signup' %}" class="nav-link">signup</a>
    <a href="{% url 'accounts:login' %}" class="nav-link">login</a>
    <a href="{% url 'accounts:logout' %}" class="nav-link">logout</a>
</nav>
```

## 7. Logout - Delete

- 데이터베이스에서 발급했던 session을 찾아서 지워줌
---
```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```

## 8. 로그인 유무에 따른 nav 구조 변경

```html
<!-- ../templates/base.html -->
<nav class="nav">
    <!-- is => True or False -->
    {% if user.is_authenticated %}
        <a href="" class="nav-link disabled">{{user}}</a>
        <a href="{% url 'accounts:logout' %}" class="nav-link">logout</a>
    {% else %}
        <a href="{% url 'accounts:signup' %}" class="nav-link">signup</a>
        <a href="{% url 'accounts:login' %}" class="nav-link">login</a>        
    {% endif %}
</nav>
```

# 게시물

## 9. startapp articles

- settings.py

## 10. Article modeling/migration

- 택 1
```python
# articles/models.py

# 1. 직접참조 -> 추천하지 않음
from accounts.models import User
user = models.ForeignKey(User, on_delete=models.CASCADE)

# 2. settings.py 변수 활용
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# 3. get_user_model
from django.contrib.auth import get_user_model
user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
```

## 11. Article - Create

- 경로 설정
- create 버튼 만들기
- Form
- 함수 생성
```python
# articles/views.py
from .forms import ArticleForm
from django.shortcuts import redirect

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # user 정보를 직접 넣어줘야함
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)
```

## 12. Article - Read

- 경로 설정
- 함수 생성
- 페이지 생성

## 13. login_required

```python
# articles/views.py
from django.contrib.auth.decorators import login_required

# decorator: 아래에 있는 함수를 실행하기 전에 위의 함수를 먼저 실행해주세요
@login_required # 로그인을 해야 접근 가능
def create(request):
```

## 14. next 인자 처리하기

```python
# accounts/views.py
def login(request):
    # /accounts/login/
    # /accounts/login/?next=/articles/create/
    next_url = request.GET.get('next')

    # next가 없을 때 => None or 'articles:index'
    # next가 있을 때 => '/articles/create/' or 'articles:index'
    return redirect(next_url or 'articles:index')
```
- or
    - 둘 중에 하나라도 1이면 1
    - 단축평가
        - 앞 True => 앞 반환
        - 앞 False => 뒤 반환

## 15. Article - Delete

- 경로 설정
- 로그인한 사용자와 게시글 작성자가 같을 때만 삭제 버튼을 볼 수 있고(html), 지울 수 있는(def) 기능 추가
```html
<!-- articles/templates/detail.html -->
{% if user == article.user %}
    <a href="{% url 'articles:delete' article.id %}">delete</a>
{% endif %}
```
```python
# articles/views.py
@login_required
def delete(request, id):
    article = Article.objects.get(id=id)
    if request.user == article.user:
        article.delete()
    
    return redirect('articles:index')
```

## 16. Article - Update

- 버튼 추가
- 경로 설정
- 기존 정보 출력
```python
# articles/views.py
@login_required
def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        pass 
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)
```
- 페이지 생성
- 저장
```python
# articles/views.py
if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', id=id)
```
- 다른 사람이 작성한 게시글을 수정하지 못하도록 코드 수정
```python
# articles/views.py
if request.user != article.user:
# 현재 로그인한 사람 != 게시물을 작성한 사람
    return redirect('articles:index')
```

## 댓글

## 17. Comment modeling/migration

```python
# articles/models.py
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

## 18. Comment - Create

- CommentForm 정의/ 불러오기/ 인스턴스화
- action 설정
- url 설정
- 함수 생성
```python
# articles/views.py
@login_required
def comment_create(request, article_id):
    # if request.method == 'POST':
    #     pass
    # else:
    #     pass
    # 댓글 작성에는 get요청이 들어오지 않기 때문에 if문 안쪽의 코드만 있으면 됨
    # 댓글 작성칸을 보여주는 건 detail 함수에서 함

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)

        # 객체를 저장하는 경우
        comment.user = request.user # 유저 정보 = 현재 로그인한 사람
        article = Article.objects.get(id=article_id) # 게시물 정보 = 현재 게시글
        comment.article = article

        # id 값을 저장하는 경우
        # DB에 저장되는 숫자를 가져옴
        comment.user_id = request.user.id 
        comment.article_id = article_id

        comment.save()

        return redirect('articles:detail', id=article_id)
```

## 19. Comment - Read

- html에서 _set.all 함수 사용

```html
<!-- articles/templates/detail.html -->

{% for comment in article.comment_set.all %}
<!-- all은 함수지만 html에서는 () 쓰지 않음 -->
    <li>{{comment.user.username}} : {{comment.content}}</li>
    <li>{{comment.user}} : {{comment.content}}</li>
    <!-- 원래 username을 적어야 하는데 user에서 편의성 기능으로 id를 출력해줌 -->
{% endfor %}
```

## 20. Comment - Delete

- 버튼 생성
- 경로 설정
- 함수 생성
- 댓글 작성자만 댓글 삭제 버튼을 볼 수 있도록 변경
```html
<!-- articles/templates/detail.html -->
{% if user == comment.user %}
    <a href="{% url 'articles:comment_delete' article.id comment.id %}">Delete</a>
{% endif %}
```
- 로그인한 사람만 댓글을 지울 수 있도록 변경
```python
# articles/'views.py'
@login_required
def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()

    return redirect('articles:detail', id=article_id)
    # if문을 통과하지 못하면 바로 return으로 이동
```

# bootstrap 편하게 쓰기

## 21. django-bootstrap

```shell
pip install django-bootstrap-v5
pip install django-bootstrap5
```
- 호환성 문제
    - v5는 장고 4버전 이하에서만 동작하기 떄문에 설치했던 장고 5버전을 지우고 4버전 재다운
- 앱 등록
```python
# auth/settings.py
INSTALLED_APPS = (
    'bootstrap5',
    'django_bootstrap5',
)
```
- 사용 방법
```html
<!-- extends 아래에 써야함 -->
{% load bootstrap5 %}
{% load django_bootstrap5 %}

{% bootstrap_form form %}
```

# Profile

## 22. user profile

- 버튼 생성
- 경로 설정
- 함수
```python
# accounts/views.py
from .models import User

def profile(request, username):
    user_profile = User.objects.get(username=username)
    # user와 충돌이 일어날 수 있으므로 이름 변경

    context = {
        'user_profile': user_profile,
        # 'user': request.user # 장고가 우리 모르게 넣어둔 것
    }

    return render(request, 'profile.html', context)
```
- 페이지 생성
```html
<!-- accounts/profile.html -->
{% extends 'base.html' %}

{% block body %}
    <h1>{{user_profile.username}}</h1>

    {% for article in user_profile.article_set.all %}
        <li>{{article.title}}</li>
    {% endfor %}
{% endblock %}
```


# 요약

0. .gitignore
    - 가상환경 생성/활성화
    - django 설치
    - .gitignore 설정

1. startproject

2. startapp
    - 앱 등록

3. base.html
    - template 등록

## bootstrap
4. django-bootstrap5
    - 설치
    - 앱 등록
    - html에 load

## 회원가입
5. User modeling/migration
    - from django.contrib.auth.models import AbstractUser
    - AUTH_USER_MODEL 등록

6. Signup - Create
    - 경로 설정
    - from django.contrib.auth.forms import UserCreationForm
    - 함수 생성
    - 페이지 생성

7. Login - Create
    - 경로 설정
    - from django.contrib.auth.forms    import AuthenticationForm
    - from django.contrib.auth import login as auth_login
    - 페이지 생성

8. Logout - Delete
    - from django.contrib.auth import logout as auth_logout

9. Navbar - If

## 게시물
10. startapp
    - 앱 등록

11. Article modeling/migration
    - from django.conf import settings
    - ForeignKey

12. Article - Create
    - 경로 설정
    - Form
    - 함수 생성
    - 페이지 생성

13. Article - Read
    - 경로 설정
    - 함수 생성
    - 페이지 생성

14. login_required
    - from django.contrib.auth.decorators import login_required

15. next 인자 처리하기

16. Article - Delete
    - 경로 설정
    - html 로그인한 사용자 == 게시글 작성자 if
    - 함수 if

17. Article - Update
    - 버튼 추가
    - 경로 설정
    - 기존 정보 출력
    - 페이지 생성
    - 새로운 정보 저장
    - 함수 if 현재 로그인한 사람 != 게시물 작성자

## 댓글
18. Comment modeling/migration
    - ForeignKey

19. Comment - Create
    - CommentForm 정의/ 불러오기/ 인스턴스화
    - action 설정
    - 경로 설정
    - 함수 생성

20. Comment - Read
    - html에서 _set.all 함수 사용

21. Comment - Delete
    - 버튼 생성
    - 경로 설정
    - 함수 생성
    - 댓글 작성자 == 삭제 html/ 함수

## profile
22. user profile
    - 버튼 생성
    - 경로 설정
    - 함수 생성
    - 페이지 생성