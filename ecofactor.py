__author__ = 'noisufnoc'

import secrets
import mechanize

url = 'https://my.ecofactor.com/mobile/login.html'

br = mechanize.Browser()
br.open(url)

br.select_form(nr=0)
br['j_username'] = secrets.username
br['j_password'] = secrets.password

results = br.submit().read()

print results

