with open("text_2.txt", "r", encoding="utf-8") as read_file:
    file_rdlns = read_file.readlines()
    print(f"Кол-во строк: {len(file_rdlns)} ")
    for count, i in enumerate(file_rdlns):
        print(f"{count+1}-ая строка: {len(i.split())} слов. ")