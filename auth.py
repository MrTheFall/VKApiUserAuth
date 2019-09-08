import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from requests import *

login = 'Your e-mail or phone number'
tokenAddress = "https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=%s&password=%s"
resp = get(url=tokenAddress % (login, ('Your Pass'))).json()

# Getting "Implicit flow" token
vk_session = vk_api.VkApi(token=resp["access_token"])
vk = vk_session.get_api()
print('done')

# To use all vk api methods use vk.METHODNAME
