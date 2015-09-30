__author__ = 'besimaltnok'
__author__ = 'octosec'

import base64

file = open("/home/besim/ctf_q/hash", "r")
read = file.read()
data = "FLAG_{"
num = 0
while (read.startswith(data) != True):
    oku = base64.b64decode(read)
    num = num + 1

print(read)
print(num)
