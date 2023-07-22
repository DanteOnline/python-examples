import time

start = time.time()

def request(url):
    time.sleep(10)


for i in range(6):
    request('http://')

end = time.time()

print(end - start)

