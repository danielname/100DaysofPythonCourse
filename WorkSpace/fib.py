def fib(n):
    starter = [0, 1]
    if n > 1:
        for number in range(2, n + 1):
            starter.append(starter[number-1] + starter[number-2])
    print(starter[n])


fib(4)
