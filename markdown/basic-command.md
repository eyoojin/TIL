Ctrl + S 습관적으로 누르기

# 1. 제목

- 1~6개의 # 기호를 사용하여 제목 수준을 지정
- 마크다운의 목적: 일관된, 표준화된 문서를 사용하고자

## 예시 중제목
### 예시 소제목

# 2. 텍스트 스타일

- 굵게: **단어**
- 기울임: *단어*
- 취소: ~~단어~~
- 굵고 기울임: ***단어***

# 3. 텍스트 인용

> 인용구문
> 여러줄도 가능

# 4. 코드 인용

- 인라인 코드 인용 => 이것은 `code` 입니다.
- 코드 블럭
```python
def hello():
    print("hello!")
```

```javascript
console.log("hello")
```
위쪽 백틱에 사용하는 언어를 적으면 언어에 맞게 색칠

# 5. 링크

- [구글](https://google.com)
- []: 가야하는 곳 이름, 사진이 안 뜰 때 보여지는 텍스트를 적는 공간
- (): 주소

# 6. 이미지

- ![강아지 사진](https://image.utoimage.com/preview/cp872722/2022/12/202212008462_500.jpg)
- ![고양이](../assets/cat.jpg)

- ..: 나보다 한단계 위 상위 폴더, 바뀜 (상대경로)
- vs (절대경로) 전체 경로를 적어줌, /c/Users/1-14/Desktop/DAMF2/TIL

# 7. 목록

## 순서있는목록

1. 첫번째
2. 두번째
3. 세번째

## 순서없는목록

- 첫번째
    - 1-1
    - 1-2
- 두번째
- 세번째

# 기타

- 상세한 내용은 slack 링크 타고 들어가서 보기
- [x] 할일목록
    git hub에서는 체크박스로 뜸
- 마크다운 문법: 노션, 옵시디언 등에 모두 적용
- 폴더는 파란색/, 파일은 흰색
- .: 현재 폴더

[출처](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# git
`git add .`
`git commit -m "{commit}"`
`git push origin master`