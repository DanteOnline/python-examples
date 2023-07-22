import time
import math

start = time.time()


def request(url):
    for i in range(100000):
        math.sqrt(math.pi)


for i in range(4):
    request('http://')

end = time.time()

print(end - start)

