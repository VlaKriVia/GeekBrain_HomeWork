class ElementTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

el = ""
my_list = []

while True:
    try:
        el = input('Введите новый элемент списка(число), или "stop", чтобы выйти из цикла')
        if el == "stop":
            break
        elif not el.isdecimal():
            raise ElementTypeError("Элемент должен быть числом!")
        my_list.append(el)
    except ElementTypeError as err:
        print(err)
print(my_list)