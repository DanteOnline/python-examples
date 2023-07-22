import time
from threading import Thread

start = time.time()
def request(url):
    time.sleep(10)

result_threads = []
for i in range(6):
    # request('http://')
    t = Thread(target=request, args=('http:/',))
    t.start()
    result_threads.append(t)

for rt in result_threads:
    rt.join()

end = time.time()

print(end - start)

