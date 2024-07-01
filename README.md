# git
Git Command Practice

# Commands
- git init (.git file 생성)
- git config --list
- git status // 현재 git 현황 체크 및 트랙킹 (커밋이나 변동사항등 저장소와 비교)
- git [명령어] --help // 명령어 사용 방법 및 리스트 확인
---
- git clone [git링크] [파일저장경로] // 저장소 내 파일 복사
- git remote add origin [git링크] // 저장소 연결
---
- git branch [새로 생성 브랜치 명] [기존 파일 복사할 부모 브랜치] // git branch 생성
- git branch -d [브랜치 명] // 브랜치 삭제
- git branch -m [브랜치 명] [새로 이름 바꿀 브랜치 명] // 기존 브랜치 이름 변경?
- git checkout [브랜치 명] // 특정 브랜치로 위치? 변경
- git rebase [브랜치 명] // 재정렬? 명령어 재확인 필요
---
- git tag [태그명] [브랜치 명] // 브랜치에 태그 붙이기
- git tag // 태그 리스트 보기
---
- git pull // 저장소 내 변동 된 파일 등 적용 (다운로드)
- git push // 본인 수정한 코드 저장소에 저장 (업로드)
---
- git add -i // 파일 스테이징 옵션
- git add [fileName] // 파일 스테이징 (커밋 전 준비 사항 / 스테이징)
- git commit -a // 스테이징 건너 뛰고 수정된 파일 전부 커밋 (all)
- git commit -m "text" -m "text" // 스테이징된 파일 커밋하기 ""당 한 개 문단 취급 (message)
---
- git log // git 커밋 내역 로그 출력
- git log -p // git 커밋 내역 변동 사항 출력 
- git diff // 이전 커밋 소스코드와의 차이점 확인
- git diff [CommitCode]..[CommitCode] // 둘의 커밋 소스코스 차이점 확인하기
---
- git reset [CommitCode] --[soft/hard/등] // 해당 커밋으로 파일 리셋 (해당 커밋 이후는 숨김 처리 -> 정보는 남아있어 복구 가능)
- git revert [CommitCode] // 뭐야 얘도 알려줘요 이게 뭔데
---
- git mv [file] [newFilePathOrName] // 리눅스 mv 마냥 파일 옮기기 