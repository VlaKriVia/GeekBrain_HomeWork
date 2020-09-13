class MyOwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:

except MyOwnZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
else:
    print(round(a/b))