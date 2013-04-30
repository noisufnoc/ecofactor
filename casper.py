import secrets
import time
from ghost import Ghost

ghost = Ghost()

page, resources = ghost.open('https://my.ecofactor.com/mobile/login.html')

result, resources = ghost.fill('form', {
    'j_username': secrets.username,
    'j_password': secrets.password
})

page, resources = ghost.fire_on('form', 'submit')
#page, resources = ghost.fire_on('form', 'submit', expect_loading=True)

page, resources = ghost.wait_for_page_loaded()

ghost.capture_to("/tmp/foo.png")


print page.http_status
#print resources