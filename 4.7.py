from functools import reduce

def fact(n):
    my_list = [i for i in range(1, n+1)]
    for el in (reduce((lambda a, b: a * b), my_list[0:i+1:1]) for i in range(n)):
        yield el

for el in fact(10):
    print(el)
