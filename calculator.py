import time

def calculator():
    memory = []
    while True:
        val = yield
        if val == 'memory':
            print(memory)
        else:
            one, two = val
            result = one + two
            print(result)
            memory.append(result)


if __name__ == '__main__':
    calc = calculator()
    calc.send(None)
    calc.send((2, 5))
    calc.send((5, 7))
    calc.send('memory')
    calc.send((1, 2))
    calc.send((4, 9))

    print('something')

    calc.send('memory')

    while True:
        time.sleep(20)
