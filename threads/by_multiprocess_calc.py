import time
import math
from multiprocessing import Process

start = time.time()


def request(url):
    for i in range(100000):
        math.sqrt(math.pi)


result_threads = []
for i in range(4):
    # request('http://')
    t = Process(target=request, args=('http:/',))
    t.start()
    result_threads.append(t)

for rt in result_threads:
    rt.join()

end = time.time()

print(end - start)

