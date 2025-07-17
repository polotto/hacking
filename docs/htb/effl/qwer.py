#!/usr/bin/env python3

import requests
import re
import hashlib

url = 'http://139.59.178.146:31272/'

s = requests.Session()

text = s.get(url).text
code = re.search('<h3.*>(.*)</h3>', text).group(1).encode('utf-8')

print(code)

result = hashlib.md5(code).hexdigest()

print(result)

data = {
  'hash': result
}

response = s.post(url, data=data, verify=False)

print(response.text)

s.close()