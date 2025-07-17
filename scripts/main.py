#!/usr/bin/env python3

import requests

url = ''
data = {
    '': ''
}

s = requests.Session()

resp = s.post(url, data=data)
print(response.text)

s.close()