import json

firm_profits = {}
average = []

with open("text_7.txt", "r", encoding="utf-8") as read_file:
    file_rdlns = read_file.readlines()
    for i in file_rdlns:
        firm_name, useless, income, outcome = i.split()
        firm_profit = int(income) - int(outcome)
        firm_profits.update({firm_name : firm_profit})
        if 0 < firm_profit:
            average.append(firm_profit)
    result = [firm_profits, {"average_profit" : round(sum(average) / len(average), 2)}]
    print(result)
with open("json_7.json", "w", encoding="utf-8") as json_file:
    print(json.dump(result, json_file))