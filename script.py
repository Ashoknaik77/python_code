import math
import sys
from os import rename

import requests

print(sys.version)


def greet(whotogreet):
    greeting = 'hello,{}'.format(whotogreet)
    return greeting


r = requests.get('http://google.com')
print(r.status_code)
print(greet('world'))
print(greet('NIVAAN'))
