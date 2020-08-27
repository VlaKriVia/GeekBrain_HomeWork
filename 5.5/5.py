import random

with open("text_5.txt", "w", encoding="utf-8") as new_file:
    print(" ".join([str(random.randint(10, 100)) + " " for i in range(random.randint(10, 20))]), file=new_file)
with open("text_5.txt", "r", encoding="utf-8") as new_file:
    print(sum(map(lambda a: int(a), new_file.read().split())))