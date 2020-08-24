import itertools

#a
def limit_count(start, end):
    start, end= int(start), int(end)
    for el in itertools.takewhile(lambda x: x < end, itertools.count(start)):
        yield el

#b
#выводит элементы списка столько раз, сколько указано в end(). обединено с первой задачей
end = int(input())
my_list = ['a', 'b', 'f']
my_list.append(None) #не изменять!
for i in limit_count(0, end):
    for el in itertools.takewhile(lambda x: x != my_list[-1], itertools.cycle(my_list)):
        print(el)
