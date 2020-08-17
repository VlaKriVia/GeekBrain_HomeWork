months_to_seasons = {12 : 'winter',
                     1 : 'winter',
                     2 : 'winter',
                     3 : 'spring',
                     4 : 'spring',
                     5 : 'spring',
                     6 : 'summer',
                     7 : 'summer',
                     8 : 'summer',
                     9 : 'fall',
                     10 : 'fall',
                     11 : 'fall',}

in_put = int(input('Напишите месяц целым числом от 1 до 12: ')) // 1
while not 1 <= in_put <= 12:
    in_put = input('Напишите месяц числом от 1 до 12: ')

print(f'Выбранный месяц принадлежит следующему времени года: {months_to_seasons[in_put]}')

months_to_seasons = [['winter', 12, 1, 2],
                     ['spring', 3, 4, 5],
                     ['summer', 6, 7, 8],
                     ['fall', 9, 10, 11]]

in_put = int(input('Напишите месяц целым числом от 1 до 12: ')) // 1
while not 1 <= in_put <= 12:
    in_put = input('Напишите месяц числом от 1 до 12: ')

for season in months_to_seasons:
    if in_put in season:
        print(f'Выбранный месяц принадлежит следующему времени года: {season[0]}')
        break
