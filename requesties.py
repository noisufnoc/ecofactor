__author__ = 'miwalker'

import requests
import secrets
import json

login_data = {
    'j_username': secrets.username,
    'j_password': secrets.password
}

s = requests.Session()
s.post('https://my.ecofactor.com/mobile/loginProcess', data=login_data)

#house_data = 10127
house_data = {'text': '[10127]'}
house_headers = {'content-type': 'application/json'}

#r = s.get('https://my.ecofactor.com/mobile/locationsInfo.html', cookies=s.cookies)

r = s.post('https://my.ecofactor.com/mobile/locationsInfo.html', data=json.dumps(house_data), headers=house_headers)

print r.text
