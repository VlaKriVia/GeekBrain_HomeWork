my_list = [7, 5, 3, 3, 2]

while True:
    print(my_list)

    num = int(input())
    if my_list[0] <= num:
        my_list.insert(0, num)
        continue

    count = 0
    for i in my_list:
        if my_list[count-1] >= num >= my_list[count]:
            my_list.insert(count, num)
            break
        count += 1

    if num < my_list[-1]:
        my_list.append(num)
