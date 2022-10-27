total = 0
count = 0
numb_of_tic = int(input("Сколько билетов вам нужно? "))
for _ in range(numb_of_tic):
    age = int(input("Сколько лет человеку, на которого покупается билет: "))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        total += 990
    else:
        total += 1390
        count += 1
if numb_of_tic >= 3:
    total = total - (total / 100 * 10)
print("%d" % total)
