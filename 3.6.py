def int_func(word):
    word = list(word)
    word[0] = word[0].upper()
    word = ''.join(word)
    print(word)
    return word

string = input().split()
f_string = []
for i in string:
    f_string.append(int_func(i))
    print(f_string)
print(' '.join(f_string))
