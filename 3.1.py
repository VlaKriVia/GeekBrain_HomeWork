def divistion(a, b):
    """Возвращает результат деления a на b
    учтена возможность деления на ноль и
    ввод неправильного типа данных"""
    try:
        a, b = int(a), int(b)
        return round(a/b)
    except ValueError:
        print("Ошибка! Введен неправильный тип данных!", end = '\n')
    except ZeroDivisionError:
        print("Ошибка! Вы подеилил на ноль!", end = '\n')

print(divistion(input("Введите делимое. "), input("Введите делитель. ")))
