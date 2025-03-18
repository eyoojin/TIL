# CRUD

## 0. setting

- 가상환경 생성/ 활성화
- .gitignore
    - python, window macOS, Django

## 1. Django

- 장고 설치
- 프로젝트 생성
- 앱 생성
- 앱 등록
- MTV
    - 경로 설정
    - 함수 생성
    - templates 폴더 생성/ html 파일 생성

## 2. CRUD
```
Create: 생성
Read: 읽기
Update: 갱신
Delete: 삭제
```

- modeling
- migration
    - 번역본 생성
    - DB에 반영
- admin 페이지에 모델 등록
- CRUD 기능 구현
    - Read all
        - index()
    - Read 1 
        - detail()
    - Create
        - new()
        - create()
    - Delete
        - delete()
    - Update
        - edit()
        - update()