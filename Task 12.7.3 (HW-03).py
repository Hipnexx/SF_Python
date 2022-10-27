money = float(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent['ТКБ']
b = per_cent['СКБ']
c = per_cent['ВТБ']
d = per_cent['СБЕР']
deposit = ["%.2F" % (money * a), "%.2F" % (money * b), "%.2F" % (money * c), "%.2F" % (money * d)]
print(deposit)
max_result = max(deposit)
print("Максимальная сумма, которую вы можете заработать -", max_result)
