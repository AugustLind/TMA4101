def fibonacci(tall):
    a = 1
    b = 1
    runde = 2
    while tall > runde:
        c = a + b
        runde += 1
        a = b
        b = c
    print(c)
fibonacci(8)
