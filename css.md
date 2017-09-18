# C~ascading~S~tyle~S~sheet~
---
금요일, 15. 9월 2017 11:43오후 

##  ~S~tyle ~S~heet
HTML에서 **(LayOut과 함께) <u>Style을 분리</u>**
HTML은 **<u>문서의 구조</u>**에 집중함 
<br>

##  ~C~ascading 
  **하나**의 HTML element - **여러** CSS 선언들
  충돌을 피하는 피하는 규칙 
  
 가. 중요도  
     ` !important`  >  `사용자 정의`  > `Browser 정의`     <br>
 나. 명시도(특정도)
      `(  CSS inline,  id,  class,  ) `   <br>
 다.  소스 순서 
<br>
 
## ~상~속 (Inherit) 

#### 참고  
1) [Appendix F. Full property table](https://www.w3.org/TR/CSS21/propidx.html)
2) [상속과 캐스케이딩](http://www.clearboth.org/28_inheritance_and_cascade/)   <br>

**상속** : **부모**~요소~  &#8212;  **자식**~요소~  : **속성값** 전달   <br>
**가.** 상속되지 **않는** 것 :
- [**inline/block**] `display`
- [**layout**] `position`, top, right, bottom, left
- [**layout**] `float`/`clear`
- [**size**] width/height, min-width, min-height, `box-sizing`
- [**box model**] padding, margin, `border`
- background, overflow  <br>

**나.** 상속하는 것 
- color
- font
- letter-spacing / word-spacing / line-height / text-align / text-indented
- `white-space` (줄바꿈)
- border-collapse <br>

다. 강제상속  `property : inherit`
<br>

## ~S~elector
[선택자 요약표 ](http://www.w3.org/TR/selectors/) 

#### Pseudo-Classes Selector 
HTML에는  존재하지 않지만 필요에 의해 가상의 선택자를 지정 

패턴 | 의미 
--|--
`E:link` | 방문하지 않은 링크 
 `E:visited` | 방문한 링크 
 `E:active` | 마우스 클릭 또는 키보드 엔터를 누르는 동안 
 `E:hover` | **마우스가 올라가 있는 동안**
 `E:focus` | 포커스가 머물러 있는 동안
 `E::first-line` | 첫번째 라인 
 `E::first-letter` | 첫번째 문자
 `E::before` | **시작 지점**에 생성된 요소
 `E::after` | **끝 지점**에 생성된 요소 
 `E:nth-child(3n+2)` | 부모의 3n+2번째 <u>**자식인 E**</u>요소 
 `E:nth-of-type(an+b)` | **같은 유형의 n번째 형제인 E요소** 
 `E:nth-last-child(n)` | 맨 마지막부터 계산하여 같은 부모의 <br> n번째 자식인 E요소
 `E:nth-last-of-type(n) | 맨 마지막부터 계산하여, 같은 유형의 <br>n번째  형제인 E요소 
 
 
 #### Chain Selector 
 한 요소에  여러 id, classs적용
~~~html
<p class="body-text description"> Lorem ipsum doloro? </p>
~~~

 
 
<br>

## ~B~ox model

* content / padding / border / margin 
* **inline element** vs block element  
     - 인라인 요소 :  size(width/height) 지정 불가능, 내용에 자동으로 맞추어짐, 가로 마진만 가질 수 있음 
       -  **inline-block**:  inline element이나 block 처럼 height, margin, padding을 지정할 수 있음 (width는 내용에 의해 정해짐)
* margin collapse : 위/아래로 겹치는 마진 
<br>

## List ~S~tyle
~~~css
ul, ol {
    list-style-type: none; 
}
~~~     

## Table ~S~tyle
~~~css
table { 
    border-collapse: collapse; 
     table-layout: auto; 
    }
tr, td {
    border: 1px solid black; 
    width: 30px; 
    text-align: center;
}
~~~
<br>

## ~F~loat ~L~ayout  
#### 자식 요소들의 <u> float: left 후 부모 요소의 height이 인식되지 않는</u> 문제:
* (ans01) 임의의 요소 삽입하여 해결
~~~html
 <div class="outer">
     <div class="inner"> A </div>
     <div class="inner"> B </div>
     <div class="inner"> C </div>
     <br style="clear: both;"> 
 </div>    
~~~
 * (ans02) 부모 요소에 `overflow: hidden;` 
 * (ans03) 부모 요소에도 `float: left;`
 * (and04)`::after` 가상선택자 사용 
 
~~~css
.outer::after {
    content: "";
    height: 0;
    display: block;
    clear: both;
}
~~~
* **Flex** 
* **CSS FrameWork** :  Bootstrap 등 
<br>

## ~P~o~s~i~t~io~n~
* `position: static`(기본값) 정적인 상태. 다른 요소에 의해 정해진다. 
* `position: relative;` : 부모 엘리먼트를 기준으로 **상대적**으로 움직인다. 
* `position: absolute;` 
    - 'relative/absolute'인 가장 가까운 부모를 기준으로 움직인다.  
    - 부모와의 관계가 끊기고 자신의 크기가 컨텐츠만 해진다.
    - `z-index`와 `fixed`와 함께 메뉴 구성에 사용됨 

<br>

## ~C~enter positioning
#### 1. 부모의 가운데로 정렬하는 방법
~~~css
/* 가로 중앙 */
.outer {
  > .inner {
     width: 500px;
     margin: 0 auto; 
  }
} 
~~~
~~~css
/* 가로, 세로 중앙 method 1*/
.outer {
  height: $y;
  line-height: $y;
  > .inner {
    width: 500px;
    margin: 0 auto;
  }
}
/* 가로, 세로 중앙 method 2*/
.outer {
  > .inner {
    position: absolute;
    width: 200px;  height: 100px;
    top: 50%;   /*calc(-100px/2);*/
    left: 50%;   /*calc(-200px/2);*/
    transform: translate(-50%, -50%);
  }
}
~~~

<br>
## 방~법~론 
#### O~bject~O~riented~CSS 
  Decoupling
  Single responsiblity
  Encapsulation 

* Contrainer와 Content의 분리 (요소와 분리)
~~~css
 h3.content-title 
 /* 위 방식 보다 아래 처럼 */
 .content-title
~~~
* Structure와 skin의 분리 
~~~css
.structure {
    display: block; 
    width: 100px;  height: 100px;
    position: relative;
    float: left; 
}
.skin {
    font: san-serif;
    color: #585858;
    border: 1px solid black;
    padding: 5px;
    margin:5px;
}
~~~

#### B~lock~E~lement~M~odifier~
* 웹페이지를 component들의 조합으로 봄
* css inline style 불허 
* id 사용 불허 

#### S~calable and~M~odular~A~rchitecture for~CSS
* Categorization 
    - Base :  Tab selector (html, body, a, input ...)
     - Layout : header / footer / content / article / section / item / aside
     - module
     - state :  is-hidden / is-collapse
      -theme : 배경, 색, 글꼴, 테두리 
     
#### 방법론은 방법론에 불과함 
* CSS는 '빠른 수정'보다 **'빠르고 잦은 테스트'**가 더 중요함 
<br>

## S~yntactically~ A~wesome~S~tylesheet~
#### CSS 전처리기(pre-processor)
* SASS --- CSS

#### sass-autocompile
* atom package
     - `Node.js`를 설치
     - `NPM`(Node Package Manager)으로 `node-sass`패키지 설치 
~~~shell
// 설치    
 sudo apt-get install -y node.js
 sudo apt-get install -y npm
// 확인 
 node -v 
  // node-sass 설치 
 sudo npm install node-sass -g
~~~     
     
* settings ( `Ctrl` + `Shift` + `p` : `settings`) 
    - Compile on Save
    - Compile with 'compressed'
    - Compile with 'compact'
    - compile with 'nested'
    - compile with 'expanded'
    - 상대 경로 지정 :  `'./css/css'`

#### sass ~S~yntax

~~~sass
 // 주석내용 
 /* 주석내용 */
 
@import './css/_reset';   
   // '_filename'은 css파일로 compile되지 않음. only import~!
@import './css/reset01'; 

 // Referencing parent selector & 
 // 부모 참조 선택자 
a {
  text-decoration: none;
  &: hover {
    color: red;
  }
} 
~~~


















