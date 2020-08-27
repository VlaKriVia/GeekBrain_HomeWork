with open("text_3.txt", "r", encoding="utf-8") as old_file:
    with open("text_3.1.txt", "w", encoding="utf-8") as new_file:
        file_rdlns = old_file.readlines()
        sum_list = []
        for i in file_rdlns:
            i = i.split()
            if float(i[1]) < 20000:
                print(i[0], file=new_file, end = " ")
            sum_list.append(float(i[1]))
        print(f'\nСредняя заработная плата = {round(sum(sum_list) / len(sum_list))}', file=new_file, end = '')