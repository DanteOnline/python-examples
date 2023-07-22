import time
import math
from threading import Thread

start = time.time()


def request(url):
    for i in range(100000):
        math.sqrt(math.pi)


result_threads = []
for i in range(4):
    # request('http://')
    t = Thread(target=request, args=('http:/',))
    t.start()
    result_threads.append(t)

for rt in result_threads:
    rt.join()

end = time.time()

print(end - start)

