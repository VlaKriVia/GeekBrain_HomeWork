data = []
new_data = {}
structure = ['название', 'цена', 'количество', 'ед']

count = 1
while True:
    data.append((count, {'название' : input(f'Введите название товара №{count} '),
                     'цена' : input(f'Введите цену товара №{count} '),
                     'количество': input(f'Введите количество товара №{count} '),
                     'ед': input(f'Введите систему исчисления товара №{count} ')}))

    end = input('Напишите "break", если законцили ввод данных. ')
    if end == 'break': break
    count += 1

for I in structure:
    category = []
    for i in data:
        if i[1].get(I) not in category:
            category += i[1].get(I)

    new_data.update({I : category})

print(new_data)
