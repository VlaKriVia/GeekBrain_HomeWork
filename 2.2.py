my_list = []
new_element = input('Вводите строки, которые будут добавлены в ваш список, или " ", чтобы завершить процесс. ')
while new_element != ' ':
    my_list.append(new_element)
    new_element = input('Вводите строки, которые будут добавлены в ваш список, или " ", чтобы завершить процесс. ')

list_count = 0
while list_count < len(my_list) - 1:
    my_list[list_count], my_list[list_count + 1] = my_list[list_count + 1], my_list[list_count]
    list_count += 2

print(f'Ваш новый список: {my_list}')
