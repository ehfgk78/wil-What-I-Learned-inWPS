# Git

## 참~고~ 
* [git-scm 문서](https://git-scm.com/book/) 
* [초심자를 위한 Github 협업 튜토리얼](https://milooy.wordpress.com/2017/06/21/working-together-with-github-tutorial/) 

## 1. Ins~T~all
* 문제상황 
     - [git-scm 문서](https://git-scm.com/book)에서 `git-all`을 하므로, Ubuntu16.04LTS에서 dependency (runit)문제가 발생함 
     - https://askubuntu.com/ : **"Problem installing package git-all" **
~~~shell
dpkg: error processing package runit (--configure):
 subprocess installed post-installation script returned error exit status 1
dpkg: dependency problems prevent configuration of git-daemon-run:
 git-daemon-run depends on runit; however:
  Package runit is not configured yet.
~~~
 
 * 다음과 같이 해결 
 [Fastcampus-WPS](https://github.com/Fastcampus-WPS-6th/Tips/blob/master/git.md) 

~~~shell
// runit과 git-daemon-run을 설정 파일까지 모두 지움
sudo apt-get purge runit
sudo apt-get purge git-all
sudo apt-get purge git
sudo apt-get autoremove
// git만 설치함
sudo apt-add-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git
~~~

## about G~i~t 
* V~ersion~C~ontrol~S~ystem~ 
 (&Delta;file, time) &rArr; 기록 &rArr; Repository(ver1 &rarr; ver2 &rarr; ver3 &hellip;)
 (&Delta;file, time) &larr; 불러옴 &larr; Repository: version X

* **L**~ocal VCS~ &rarr; **C**~entral VCS~ &rarr;  **D**~VCS~
 &ndash; L~ocal VCS~ :  **Local** Only 
 &ndash; C~entral VCS~ :  client~local~  &harr; **Server**~central~ :  서버 중심 
 &ndash; **D~VCS~ (분산 버전 관리) ** :  **Local** is almost Everything~! 
&ndash; &ndash; client ( **Local** repository)가 server (**Remote** repository)의 데이트를 전부 복제함 
* Git의 목표 (1. 빠른 속도   &ndash;  2. 단순 구조   &ndash;  3. 비선형 개발  &ndash;  4. 대형 프로젝트 ) 
* **핵심** : &nbsp;  `~~'File 자체의 변화' ~~ ` &rArr;  `'File System 스냅샷'` 
 스냅샷 당시 File System에서,  
  &ndash;  <u>변경되지 않은</u> 파일은 링크만 저장함 
  &ndash; <u>변경된</u> 파일을 새롭게 저장함 

* How?  
 &ndash; 파일의 4가지 상태 
`untracked` &rarr; `tracked/modified` &rarr; `staged` &rarr; `commited`
 &ndash; untracked 
 &ndash;  **Working Directory** : 파일 작성 및 수정 `git status`
 &ndash; **Staging Area** : 스냅샷 &rarr; `git status`
 &ndash; **Repository**('.git directory') : commit하여 기록 &rarr; `git log` 
---
<br>

## 2. 최초 설정 `git config`
~~~bash
// etc/gitconfig 파일 : 해당 시스템의 모든 사용자와 모든 저장소에 적용
$ git config --system

//  ~/.gitconfig  또는 ~/.config/git/config
$ git config --global 
~~~

~~~bash
// 사용자 정보 
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

// 편집기 설정 
$ git config --global core.editor vim

// .gitignore
$ git config --global core.excludesfile ~/learn/.gitignore

// git 설정 확인 
$ git config --list

// 도움말 
$ git help <verb> 
$ git <verb> --help
~~~
<br>

## 3. G~i~t 저장소 만들기 `git init` 

### 가. `git init`
~~~bash
$ cd ~/(원하는 작업 장소) 
$ git init   // make .git

$ git add <filename>   // untracted >> tracted : 
$ git commit -m '1st commit'
~~~
### 나. `git clone`
~~~bash
// git clone [URL] 
$ git clone https://github.com/libgit2/libgit2 
~~~
<br>

## 4. G~i~t의 기초 
*  `git status` :  untracted &rarr; modified &rarr;  staged : 파일상태 확인
* `git add <filename>` : 새로 추적하기 
++ '파일시스템의 스냅샷'을 찍음 
++ commit할 스냅샷.  
++ 즉, 스냅샷은 commit 당시가 아니라  add 당시의 것이다.
 <br>
* `./gitignore` : 파일 무시하기 
++ 자동화 : ** [gitignore.io](https://www.gitignore.io/) **
++ [표준 Glob 패턴 ](https://en.wikipedia.org/wiki/Glob_(programming))을 사용함 :  `# * ! /`의 조합 
~~~bash
# 확장자가 .a인 파일 무시
*.a

# 윗 라인에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않음
!lib.a

# 현재 디렉토리에 있는 TODO파일은 무시하고 subdir/TODO처럼 하위디렉토리에 있는 파일은 무시하지 않음
/TODO

# build/ 디렉토리에 있는 모든 파일은 무시
build/

# doc/notes.txt 파일은 무시하고 doc/server/arch.txt 파일은 무시하지 않음
doc/*.txt

# doc 디렉토리 아래의 모든 .pdf 파일을 무시
doc/**/*.pdf
~~~
<br>

* `git diff` 상태 비교 
++  `git diff` :  staged vs unstaged <br>
++ `git diff --staged`:  staged vs committed 

* 파일 삭제하기 
++  1) `git rm <tracked filename>`
++ 2) `git commit`  <br>
++ git의 추적상태에서만 벗어나기 : `git rm -cashed <tracked filename>`
~~~bash
$ git rm log/ \*.log
~~~

* 파일 이름 변경하기 `$ git mv file_from file_to`
~~~bash
// git mv README.md  README는 다음과 같다. 
$ mv README.md README
$ git rm README.md
$ git add README
~~~
<br>

* commit 히스토리 조회  `git log`
~~~bash
$ git log
$ git log -p -2
$ git log -stat
$ git log --oneline --graph --all
~~~

* **되돌리기 **

++ **완료한 커밋** 수정 : 커밋 메시지를 잘못 적었을 때/ 너무 일찍 커밋했을 때 
```bash
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend
```
++ **staging Area** &rarr; **Working directory** 
```bash
$ git status
$ git reset HEAD CONTRIBUTING.md
```
++ **Modified file** 되돌리기 
```bash
$ git status
$ git checkout -- CONTRIBUTING.md
```

++ commit 하기 전 modifed file을 놓아 둔 채 다른 작업을 하려면 : `git stash`
<br>

## 5. Remote Repository









