# 리눅스 기본명령어

## 0. 명령어의 기본형식

```
command [option] [arguments]
```
- command: 실행할 명령어, 프로그램
- options: 명령어의 옵션. 주로 -로 표시됨
- arguments: 명령어에 전달할 인자

- command = python
- -V = option or arguments
- 띄어쓰기 매우 중요함!
- 엔터 치고 나서 문장을 꼭 읽어볼 것 뭐라고 대답하는지
- 대괄호 : 들어갈수도 아닐수도

## 1. 파일 및 디렉토리(폴더) 관리

- 터미널이라는 환경에서 조작

### ls (list)

- 디렉토리 내용 목록을 보여줌
- options :
    - `-l` : 파일의 상세 정보 표시 
    - `-a` : 숨김 파일 표시

- .: 현재폴더
- ..: 상위폴더
- . 은 숨겨져있기 때문에 -a를 해야 보임

### cd (change directory)

- 현재 작업 디렉토리를 변경
- `cd {target-directoty}`
    - target-directory 는 자동완성 기능을 활용 (TAB)

### pwd(print working directory)

- 현재 작업 중인 디렉토리의 전체 경로를 출력

- 내가 어디에 있는지 항상 위치를 체크할 것

### mkdir (make directory)

- 새로운 디렉토리를 생성.
- `mkdir {directory-name}`

- {} 안에는 어떤 단어를 넣어야함

### touch

- 새로운 파일을 생성
- `touch {file-name}`

### rm (rmove)

- 파일이나 폴더를 삭제
- options
    - `-r` : 디렉토리와 그 내용을 재귀적으로 삭제

    - recursive

### cat (concatenate)

- 파일의 내용을 출력

## 주의

- 한글 안 쓰기
- 대소문자 구분
- 띄어쓰기 잘하기
