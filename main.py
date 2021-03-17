# -*- coding: utf-8 -*-
from fbchat.models import *
from fbchat import log, Client
import json
import time
# list_emails = ['phimtonghop37@gmail.com',
#                'duc.nt161113@sis.hust.edu.vn', 'voccer.it@gmail.com']
email = 'voccer.it@gmail.com'

password = ''
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"

# Load session đăng nhập từ trước nếu co
session_cookies = ''
try:
    with open('session/session_gen_{}.json'.format(email)) as f:
        session_cookies = json.load(f)
except Exception as e:
    print(e)

client = Client(email, password, user_agent=user_agent,
                session_cookies=session_cookies)
while True:
    client.send(Message(text='hello'),
            thread_id='100009594708355',
            thread_type=ThreadType.USER
            )
    time.sleep(10)    
