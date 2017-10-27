import json
from urllib.request import urlopen

import requests


jenkins_json_url = "http://jenkins.dasannetworks.com/api/json?pretty=true"

# 내장 라이브러리를 사용할 때
def print_jenkins_folder():
    response = urlopen(jenkins_json_url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    for job in data['jobs']:
        print(job['name'])

# requests 외부 라이브러리를 사용할 때
def print_jenkins_folder2():
    response = requests.get(jenkins_json_url)
    data = response.json()
    for job in data['jobs']:
        print(job['_class'])



print_jenkins_folder2()