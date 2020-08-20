def my_funk(x, y):
    """Возвращает положительное число x в степень отрицательного числа y.
    Учтена возможность ввода неправильного типа данных"""
    try:
        x, y = int(x), int(y)
        if x < 0 or 0 < y:
            print("")
            return
        return round(x**y, 3)
    except ValueError:
        print("Ошибка! Введён неправильный тип данных!", end = '\n')
