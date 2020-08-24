my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list.append(None)
new_list = [my_list[i] for i in range(len(my_list) - 1) if not (my_list[i] in my_list[0:i:1] + my_list[-1:i:-1])]
print(new_list)
