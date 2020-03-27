#usr/local/bin/python3.8

import json
import AWSIoTPythonSDK

#json path
PATH = '/Users/gimsehwan/Downloads/msgjson.json'


with open(PATH,"w") as json_file:
    json_data = json.load(json_file)


