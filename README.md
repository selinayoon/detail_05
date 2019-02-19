#### 1.Django Setting을해준다

#### 2.base.html 구성

```
명세에 맞춰서 구성해준다.
이때 부트 스트랩에 그리드를 이용해 좌우로 정렬해준다.
```

```text
파비콘 추가하기

https://convertico.com/ 사이트에서 파비콘파일로 컨버팅후 알맞은 경로에 저장

​```txt
/static/images/logo.ico
​```

```

#### 3.페이지 구성

##### 헤더와 푸터

```text
시맨틱 태그를 이용해 페이지를 구성해준다.
header 와 footer 태그를 이용해 작성해준다.
footer의 class에서 좌우 padding을 준다.
```

##### signup페이지

```text
그리드를 이용해 두개의 block으로 나눠준다.
```

##### mypage페이지

```text
좌측은 Bootstrap Card를 활용해서 구성
.rounded-circle을 사용해서 원형으로 표시한다.
.position-fixed를 사용해서 스크롤을 아래로 내리더라도 좌측에 그대로 유지시켜서 사용자에게 보여줍니다.
```

##### qna페이지

```text
Bootstrap From을 사용해서 960px을 기준으로 다른 화면을 보여준다.
```

##### error페이지

```text
경로가 다른 요청이 들어왔을때 variable routing을 활용하여 사용자가 잘못 입력한 경로를 표시해주는 사이트를 만들어준다.
```

읽어주셔서 감사합니다.