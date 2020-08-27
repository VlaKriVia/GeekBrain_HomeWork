nums_dict = {"One" : "Один",
             "Two" : "Два",
             "Three" : "Три",
             "Four" : "Четыре",}
#без переводчика, мы этот модуль ещё не прошли

with open("text_4.txt", "r", encoding="utf-8") as old_file:
    with open("text_4.1.txt", "w", encoding="utf-8") as new_file:
        file_rdlns = old_file.readlines()
        for i in file_rdlns:
            i = i.split()
            i[0] = nums_dict.get(i[0])
            print(" ".join(i), file=new_file)