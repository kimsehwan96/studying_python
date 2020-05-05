from flask import Flask, request, make_response

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