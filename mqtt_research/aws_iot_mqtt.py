import logging
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

#end point, host , certs define

# host -> endpoint of aws iot
host = 'a1xhdkwmknid41-ats.iot.us-west-2.amazonaws.com'
rootCAPath = '/Users/gimsehwan/Downloads/mac_os_iot_certs/RootCA1.pem'
certificatePath ='/Users/gimsehwan/Downloads/mac_os_iot_certs/c586cd1dab-certificate.pem.crt'
privatecerificatePath = '/Users/gimsehwan/Downloads/mac_os_iot_certs/c586cd1dab-private.pem.key'
port = 8883 # not websocket/ TLS SSL
clientId = 'iotconsole-1584544032777-2'
# for test I wrote test/mac
topic ='test/mac'




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

while True:
    message = {}
    message['message'] = 'Hello, this is awsiot mqtt test'
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    print('Published topic %s: %s\n' % (topic, messageJson))
    loopCount += 1
    time.sleep(1)




