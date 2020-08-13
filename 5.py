proceeds = input("Введите доход фирмы: ")
cost = input("Введите убыль фирмы: ")

if proceeds < cost:
    print("убыток")
else:
    print("прибыль")
    print(f"рентабельность выручки равна {proceeds - cost}")
    num_workers = input("Введите кол-во сторудкиков фирмы: ")
    print(f"прибыль фирмы в расчете на одного сотрудника равна {proceeds // num_workers}")