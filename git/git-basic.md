# Git 기본 개념

## 분산 버전 관리 시스템

- 클라이언트 *(내 컴퓨터)*와 서버 *(Git Hub)* 모두가 똑같은 데이터를 유지하여 버전을 관리하는 시스템

## 파일의 세 가지 상태

- ![areas](../assets/areas.png)
- 영역
    - working directory: 내가 작성하고 있는 코드, 파일
    - staging area: add 명령어로 무대 위로 올라간 파일들
    - .git directory(repository): commit 명령어로 찍힌 스냅샷들을 저장
    - *자주 하는 실수: add를 안 하고 commit을 하는 경우. terminal을 보고 확인할 것*

## 파일의 라이프 사이클

- ![lifecycle](../assets/lifecycle.png)
- Tracked(관리대상임), Untracked(관리대상이 아님)
    - Tracked 파일: 이미 스냅샷에 포함돼 있던 파일 
        - Unmodified(수정하지 않음), Modified(수정함), Staged(커밋으로 저장소에 기록할)
    -  Untracked 파일: workin directory에 있는 파일 중 스냅샷에도 Staging Area에도 포함되지 않은 파일

## 기타

- [ ][ ]: optional
- config: configuration 초기 설정하기
- global(전역, 컴퓨터 전체) vs local
- `rm -rf` 
    - rm: 지우기
    - r: 파일과 폴더
    - f: 강제로