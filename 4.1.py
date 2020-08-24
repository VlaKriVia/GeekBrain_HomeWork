from sys import argv

try:
    adress, output_per_h, rate_per_h, premium = argv
    output_per_h, rate_per_h, premium = int(output_per_h), int(rate_per_h), int(premium)
except ValueError: print("Ошибка!! ")
print((output_per_h * rate_per_h) + premium)
