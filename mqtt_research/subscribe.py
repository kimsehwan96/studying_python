# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code" + str(rc))
    client.subscribe("hello/world")

def on_message(client, userdata, msg):
    print("Topic: ",msg.topic + '\nMessage' + str(msg.payload))

client = mqtt.Client()        # MQTT Client 오브젝트 생성
client.on_connect = on_connect     # on_connect callback 설정
client.on_message = on_message   # on_message callback 설정

client.connect("test.mosquitto.org", 1883, 60)   # MQTT 서버에 연결

# 네트웍 트래픽을 처리, 콜백 디스패치, 재접속 등을 수행하는 블러킹 함수
# 멀티스레드 인터페이스나 수동 인터페이스를 위한 다른 loop*() 함수도 있음
client.loop_forever()

#client.loop_forever() ->인터럽트가 있기 전까지 계속 브로커와(mqtt)서버와 통신하면서
#자신이 구독한 topic에 해당하는 내용이 client가 브로커에게 중개하면, subscriber는 브로커애게서 중개 받는다.

