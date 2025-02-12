# 명령어 정리

## `git init`

- 현재 디렉토리에 `.git` 폴더를 생성하여 새로운 git 저장소를 초기화

---
- `pwd`: 현재 나의 위치 확인

## `git clone`

- 현재 디렉토리에 원격저장소 폴더를 복제
```
git clone {remote url}
git clone {remote url} {directory_name}
```

## `git status`

- 현재 git의 상태를 확인
    - tracked, untracked 파일을 구분하여 표시


## `git add`

- working directory에서 변경된 파일을 staging area에 이동
```
git add {file_name/directory_name}
git add . => 현재 나의 위치를 기준으로 모든 파일과 폴더
```

## `git commit`

- stage area에 있는 변경사항을 커밋하여 스냅샷 생성
```
git commit -m "{commit}"
```

## `git log`

- 커밋의 히스토리를 조회
    - option
        - `--oneline`
        - `--graph`


## `git remote`

- 원격저장소 관리 명령어
- 원격저장소 추가
    - 일반적으로 remote_name은 `origin` 사용
```
git remote add {remote_name} {remote_url}
```
- 원격저장소 확인
```
git remote -v
```
- 원격저장소 삭제
```
git remote remove {remote_name}
```

## `git push`

- 원격저장소에 커밋을 업로드
```
git push {remote_name} {branch_name}
git push origin master
```

## `git pull`

- 원격저장소의 커밋을 다운로드
```
git pull {remote_name} {branch_name}
git pull origin master
```

## `git branch`

- `git branch`: branch 목록 확인
- `git branch {branch_name}`: branch 생성
- `git branch -d {branch_name}`: branch 삭제

## `git switch`

- `git chechout {branch_name}`: branch_name으로 이동
- `git switch {branch_name}`: branch_name으로 이동 (최신 명령어)

## `git merge`

- `git merge {target_branch_name}`: 현재 branch로 target_branch_name을 가져와서 병합
