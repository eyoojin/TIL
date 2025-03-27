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

```html
<!-- ../templates/base.html -->
<div class="container">
    {% block body %}
    {% endblock %}
</div>
```
```python
# auth/settings.py
BASE_DIR / 'templates'
```

# 회원가입/로그인/로그아웃

## 4. User modeling/migration

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
```python
# auth/urls.py
from django.urls import include

path('accounts/', include('accounts.urls'))
```
```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [path('signup/', views.signup, name='signup')]
```
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
```python
# accounts/views.py
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
```