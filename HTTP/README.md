# HTTP (HyperText Transfer Protocol)

    HTTP는 서버와 클라이언트가 텍스트, 이미지, 동영상등의 데이터를 주고 받을 때 사용하는 포로토콜이다.
    오늘날 웹을 구성하는 포로콜이다.
    텍스트 기반의 데이터로는 `HTML, CSS, javascript` 등이 있다. 
    웹서비스에 동장학는 요소 외에 HTTP(S)로 주고 받는 데이터로는 `JSON, XML`이 있다.
    웹으로 보는 이미지, 영상, 파일 같은 바이너리 데이터도 HTTP멀티파트나 `Base64`로 인코딩 하여 사용한다.
    `JSON`등을 `HTTP`와 함께 사용하는 `RESTful API` 가 있다.

## 무상태성
    HTTP는 요청 메시지를 보내기 직전까지 대상 컴퓨터가 연결 가능한지, 메시지를 
    응답 할 수 있는 상태인지 알 방법이 없다. 그래서 `stateless` 프로토콜이라고 한다.
    클라이언트가 서버로 HTTP요청을 보내면 서버는 이에 대한 응답을 보낸 다음 바로 소켓 연결을 닫는다

    모든 HTTP는 요청과 응답이 일대일로 대응되어야 하므로 요청을 받은 서버는 반드시 응답을 보내야만 한다
    클라이언트는 항상 자신이 보낸 요청이 실패했는지, 정상적으로 왔는지 알 수 있어서 로직이 단순해진다.

    그러나 클라이언트는 서버로 HTTP요청을 보내기 직전까지 실제로 서버가 동작하는지 알 방법은 없다.
    서버가 요청을 받더라도 클라이언트가 지정했던 시간 안에 응답을 보내지 못할 수 있어서 클라이언트는 각 상황에 대해 어떻게
    처리 해야 할 것 인지 결정해야 한다.

    TCP는 HTTP와 달리 연결을 끊지 않고 명시적으로 연걸을 끊기 전(소켓을 닫기 전)까지 메시지를 계속 주고 받는다.
    TCP는 텍스트가 아닌 바이너리 데이터를 사용하고, HTTP는 TCP프로콜 텍스트 기반의 HTTP 헤더와 메시지까지 사용하기 때문에
    패킷 크기가 상대적으로 크다. TCP패킷은 상대적으로 가벼워서 많은 사용자를 처리 할 수록 TCP가 HTTP보다 빠르다.

    하지만 HTTP는 각 요청이 소켓 1개를 점유하기 떄문에 문제가 생기지 않는데, TCP의 경우 여러 요청이 소켓 1개를 공동으로 사용하기 때문에 모든 요청이 1개의 소켓 안에 섞여서 이 부분에 대한 로직은 복잡해지게 된다.



## simple_sever.py
### flask 이용

    Hypertext Transfer Protocol
    GET / HTTP/1.1\r\n
    Host: 127.0.0.1:5000\r\n
    Connection: keep-alive\r\n
    Cache-Control: max-age=0\r\n
    Upgrade-Insecure-Requests: 1\r\n
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
    Sec-Fetch-Site: none\r\n
    Sec-Fetch-Mode: navigate\r\n
    Sec-Fetch-User: ?1\r\n
    Sec-Fetch-Dest: document\r\n
    Accept-Encoding: gzip, deflate, br\r\n
    Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7\r\n
    Cookie: isNotIncognito=true\r\n
    \r\n
    [Full request URI: http://127.0.0.1:5000/]
    [HTTP request 1/1]
    [Response in frame: 15]

### 와이어 샤크로 loopback 캡쳐 내용.
### 가장 첫 줄은 요청 줄이라고 부르는데 요청줄은 반드시 다음과 같은 규격이여야 한다.
### `<요청 메서드> <url 경로> <HTTP 버전> \r\n`

    요청메서드, URL, HTTP버전은 반드시 순서대로 명시하고 각 요소 사이는 공백 한칸으로 구분한다.
    위 패킷은 GET메서드, 루트(/) 경로, 1.1버전을 사용했다는 의미이다. 
    두번째 줄부터 차례대로 Host, Connection, Cache-Control 등 정보들이 있는데 이는 HTTP헤더라고 표현하며
    요청에 대한 추가 설정을 의미한다. 헤더의 순서는 바뀔 수 있다.
    마지막 Cookie 뒤에 \r\n\r\n 이 있는데 이는 헤더와 메시지 바디 경계를 구분하기 위해 사용하는 구분자이다.
    Cookie는 마지막 헤더이며 이 뒤에 오는 데이터는 메시지 바디다. (여기서는 메시지 바디가 없다.)

## 요청메서드(GET, POST, DELETE, PUT)

# GET

    요청 메서드는 요청의 형태를 정의하는 키워드 이다.
    GET메서드는 읽기 요청에 해당하므로 메시디 바디를 넣을 수는 없다. 대신 요청 주소에 ?와 & 문자로 구분자를 사용, 쿼리 파라미터를 추가 가능하다. ? 문자는 첫 번째 파라미터를 구분 할 때, & 문자는 파라미터 사이를 구분할때 사용 한다.

실제 URL 예시

### ` https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=hello+world&oquery=%EC%95%88%EB%85%95&tqi=UrskNlp0YidsshMqJHhssssssXw-427212 `

자세히 보면 search.naver 뒤 ? 문자로 부터 첫번째 파라미터가 시작 된다. sm = tab_hty.top & where = ~~~ 이런식으로 <br>
sm이라는 파라미터의 값, where이라는 파라미터 값, query 라는 파라미터의 값이 뒤에 작성된다.

# POST

    POST메서드는 클라이언트에서 서버로 데이터가 포함된 요청을 보낼 때 사용한다. 일반적으로 ID와 비밀번호로 로그인을 하거나
    상품을 장바구니에 담고 주문을 요청하는 과정에서 POST를 사용한다.

# DELETE와 PUT

    DELETE는 데이터의 삭제, PUT은 이미 존재하는 데이터의 업데이트 요청을 의미하고 기술적으로는
    POST와 큰 차이가 없다. 두 메서드는 RESTful API에서 많이 사용한다.


# URL

    URL(Uniform Resource Locator)는 웹 주소, 요청 주소라고 하며 HTTP에서 통신할 대상 컴퓨터를 식별 할 때 사용한다.
    URL주소는 사람이 식별하기 쉽게 만든 주소이고 실제로 통신 할 때는 IP기반. 따라서 DNS서버가 이 URL주소를 IP로 변환하는 작업을 한다. KT DNS ip는 168.126.63.1 이 있고... 해외 DNS서버도 있는데 대표적으로 플레어넷(?)의 1.1.1.1 그리고 8.8.8.8도 존재하고...

    URL은 주소와 경로로 나눠 표기 할 수 있는데 주소는
    http:// 혹은 https://로 시작하고 / 로 끝난다. / 이후는 경로라고 이야기를 한다.

    예 : http://helloworld.com/<경로>/<경로2>/<파일>

    cf. URI는 Uniform Resource Identifier 라고 한다. 특정 문서 영상등과 같이 자원의 위치를 가리 킬 때 사용하는 용어

# HTTP 요청 헤더

## HOST
    Host 헤더는 URL 경로를 제외한 주소가 저장된다. 포트 번호도 함께 넣을 수 있지만 필수 정보는 아니다. 
    포트 정보가 없다면 default인 80 혹은 443을 사용한다.

## Accept
    Accept 헤더는 클라이언트가 처리 할 수 있는 데이터 형태를 알려주는 키워드를 저장한다.
    단순한 텍스트부터, JSON, 동영상, 이미지 등 여러가지 종류가 있다.
    Accpet-<~~> 의 헤더도 여럿 있다.

## User-Agent
    User-Agent는 실무에서 가장 많이 사용하는 헤더이고
    HTTP 요청이 발생한 웹 브라우저 프로그램 정보가 있기 때문에 그렇다.

    웹 서비스는 브라우저마다 지원하는 표준이 조금씩 다르고 지켜야할 표준이 너무 많다.
    보통 크롬을 기준으로 개발한다.

    simple_server2.py 에서 어떤 브라우저에서 요청이 왔는지 확인하는 코드가 작성되어있음

`user agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
127.0.0.1 - - [04/May/2020 23:05:06] "[37mGET / HTTP/1.1[0m" 200 -`

Mac Os, Chrome 접속시 다음과 같은 내용이 콘솔 로그로 찍힌다.

## Content-Type 

    Content-Type 헤더에는 요청 데이터, 즉 메시지 바디의 형식을 알 수 있는 키워드가 들어간다.
    웹 서비스 개발 시 사용자 요청에 대한 응답을 보낼 때는 반드시 Content-Type 을 정확히 명시해야 한다.
    Content-Type에 따라 브라우저의 동작이 바뀔 수 있기 때문이다.
    만약 javascript가 메시지 응답에 없을 경우. text/javascript를 넣을 필요가 없다.
    만약 악성 스크립트를 해커가 json 파일인 것 처럼 위장하고 누군가에게 다운로드 받도록 한다면.
    이 script가 실행 될 우려가 있기 때문에, text나 json만 주고 받는다면 정확히 쓰는 것들만 명시하도록 한다.
## Connection:keep-alive

    HTTP 1.1버전부터 지원하며 요청/응답마다 소켓 연결을 끊는 비 효율적인 구조를 개선하기 위한 헤더 정보이다.
    keep-alive가 설정 된 경우 요청을 받은 서버는 응답을 보낸 후 타임아웃 시간 전까지 소켓 연결을 끊지 않는다.
    이 시간이 지나기 전에 동일한 클라이언트가 다시 요청한다면, 새 소켓을 사용하지 않고 기존 소켓을 사용하기 때문에
    같은 클라이언트와 주기적으로 정보를 주고 받은 경우 연결을 맺는데 쓸 시간을 줄일 수 있고 새 소켓을 낭비하지 않는다.


## 메시지 바디

    메시지 바디는 실질적인 요청 데이터를 담는데 사용한다. ID, 비밀번호, 게시판에 올릴 글 등 실제로 보낸 여러 메시지가 바로 이곳에 저장된다. HTTP로 바이너리를 보낼 때 Base64로 인코딩 한다.


# HTTP 응답


    Hypertext Transfer Protocol
    HTTP/1.0 200 OK\r\n
    Content-Type: text/html; charset=utf-8\r\n
    Content-Length: 15\r\n
    Server: Werkzeug/0.16.0 Python/3.7.4\r\n
    Date: Tue, 05 May 2020 07:37:27 GMT\r\n
    \r\n
    [HTTP response 1/1]
    [Time since request: 0.001196000 seconds]
    [Request in frame: 87]
    [Request URI: http://127.0.0.1:5000/]
    File Data: 15 bytes
    Line-based text data: text/html (1 lines)

HTTP 응답은 첫 줄과 헤더 몇개만 다르고 전체적인 구조는 비슷하다.
첫 줄에는 HTTP 버전, 상태코드(200), 상태 메시지(OK)가 차례대로 오고 각 요소는 HTTP와 동일한 방법인 공백을 사용하여 구분한다.

## 상태 코드와 메시지
    모든 HTTP 응답에는 상태 코드와 상태 메시지가 있다. 클라이언트는 이 코드로 요청이 정상적으로 처리 됐는지 알 수 있다. 요청을 정상적을오 처리하면 서버는 코드 200과 OK를 응답으로 보낸다. 
    200 : 요청 성공
    201 : 리소스를 성공적으로 생성 했을 때
    404 : Not found
    500번대 -> 웹 서버 내부 또는 웹 서버를 구성하는 다른 내부 서버에서 에러가 발생 할 때

## 세션과 쿠키

    상태라는 개념이 존재하지 않는 HTTP는 보낸 요청에 대한 응답은 구분이 가능하지만, 이전에 어떤 요청을 보냈는지 구분이 불가능 하다. 요청 헤더의 Host값을 사용하면 구문이 가능하지만 완벽하진 않다. HTTP 웹 서버는 쿠키와 세션 ID를 사용해 클라이언트를 구분한다.
    Nginx에서는 sessionId라는 이름으로, 아파치에서는 jsessionid 라는 이름으로 저장이 된다.

```python3
rom flask import Flask, request, make_response

import uuid

app = Flask(__name__)

@app.route('/')
def hello_wolrd():
    cookies = request.cookies
    # Ngnix에서는 sessionId로, Apach에서는 jsessionid를 사용한다. 기억하기
    if 'sessionId' in cookies:
        response = make_response('기존 연결 : sessionId = {}'.format(cookies['sessionId']))
    else:
        new_session_id = str(uuid.uuid4())
        response = make_response(
            '새 연결 입니다. : sessionId = {}'.format(new_session_id)
        )
        response.set_cookie('sessionId', new_session_id )
    return response

app.run()

# 세션 ID를 저장하는 sessionId 이름이나 사용하는 값은 프로그래밍 언어, 소프트 웨어 프레임 워크마다 다를 수 있다.
# 이 때는 OAuth 토큰 등을 이용해서 확인해야 한다 ~ 
```

