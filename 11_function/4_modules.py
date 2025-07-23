import math
import my_own_module
my_own_module.hello()
print(math.sqrt(8))

import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.text)
print(my_own_module.__doc__)