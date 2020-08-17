in_put = input().split()
count = 1
for i in in_put:
    print(f'{count}. {i[0:10:1]}')
    count += 1
