#у меня этот скрипт пропал, перенаписан на скорую руку
with open("text_1.txt", "w", encoding="utf-8") as new_file:
    line = input("Вводите строки. ")
    while line != "":
        print(line, file=new_file)
        line = input("Вводите строки. ")
with open("text_1.txt", "r", encoding="utf-8") as new_file:
    print(new_file.read())