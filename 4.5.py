import functools

print(functools.reduce(lambda a,b : a * b, [i for i in range(200, 1001) if i % 2 == 0]))
