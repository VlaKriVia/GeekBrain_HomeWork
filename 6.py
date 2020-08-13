starting_num = int(input("Введите начальное количество километров: "))
final_num = int(input("Введите конечное количество километров: "))
count = 1

print(f"{count}-й день: {starting_num:.2f}")
while(starting_num <= final_num):
    count += 1
    starting_num *= 1.1
    print(f"{count}-й день: {starting_num:.2f}")
print(f"Ответ: на {count}-й день спортсмен достиг результата — не менее {final_num} км.")