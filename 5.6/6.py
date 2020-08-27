def nums_only(s):
    """Принимает строку, возвращает только числа и пробелы из этой сторки в том же порядке. """
    new_s = ""
    for j in s:
        if j in "1234567890 ":
            new_s += j
    return new_s

def not_empty(l):
    """Принимает список, возвращает все елементы, кроме "". """
    new_l = []
    for j in l:
        if j != '':
            new_l.append(j)
    return new_l

with open("text_6.txt", "r", encoding="utf-8") as read_file:
    file_rdlns = read_file.readlines()
    subject_dict = {}
    for i in file_rdlns:
        i = i.split()
        subject_dict.update({i[0][:-1] : sum(map(lambda x : int(x), not_empty(map(nums_only, i[1::1]))))})
    print(subject_dict)