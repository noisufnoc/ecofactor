__author__ = 'miwalker'

import requests
import secrets

login_data = {
    'j_username': secrets.username,
    'j_password': secrets.password
}

s = requests.Session()
s.post('https://my.ecofactor.com/mobile/loginProcess', data=login_data)

r = s.get('https://my.ecofactor.com/mobile/locationsInfo.html', cookies=s.cookies)

