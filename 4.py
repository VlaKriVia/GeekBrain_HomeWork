in_put = int(input())
len_check = in_put
num_len = 1

while (True):
    if len_check <= 10:
        break
    else:
        len_check //= 10
        num_len += 1

max = (in_put // 10 ** num_len) % 10
num_len -= 1

while (0 < num_len):
    if (in_put // 10 ** num_len) % 10 > max:
        max = (in_put // 10 ** num_len) % 10
    num_len -= 1

print(max)