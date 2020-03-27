import logging
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#end point, host , certs define

# host -> endpoint of aws iot
host = 'a1xhdkwmknid41-ats.iot.us-west-2.amazonaws.com'
>>>>>>> master
rootCAPath = '보안'
certificatePath ='보안'
privatecerificatePath = ''
port = 8883 # not websocket/ TLS SSL
clientId = 'iotconsole-1584544032777-2'
# for test I wrote test/mac
topic ='test/test'




AllowedActions = ['both', 'publish', 'subscribe'] #구독/게시 혹은 게시, 구독 mqtt protocol

def customCallback(client, userdata, message):
    print("Recived data :")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("----------\n\n")


# config logger

logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# init aws mqtt client

myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privatecerificatePath, certificatePath)


# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

#start connect

myAWSIoTMQTTClient.connect()

loopCount = 0


# config custmoized json file.

json_file = [{
    "message" : "Hello from AWS IoT console",
    "sensor" : "기",
     "Input" : "50mA"
            }]

#object in python -> json object
json_string = json.dumps(json_file)

# top-level array element test

json_file_root_array = '''[
    "message": "Hello from AWS IoT console",
    "name": "1212sdf3jkk2k",
    "in": "gksdlfgjsdifgdsmmM@@@"
  ]'''




while True:
    message = {}
    message['message'] = 'Hello, this is awsiot mqtt test'
    message['sequence'] = loopCount
    #messageJson = json.dumps(message)
    messageJson = json_string

    myAWSIoTMQTTClient.publish(topic, messageJson, 1)   # 데이터 퍼블리싱
    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(5)



