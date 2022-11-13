# вводные данные
sequence_numbers = input('Введите последовательность чисел через пробел: ')
sequence_numbers = sequence_numbers.split()
list_sequence_numbers = [int(item) for item in sequence_numbers]
list_sequence_numbers.sort()
user_number = int(input('Введите любое число: '))

# двоичный поиск
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

# индексы ближайших чисел
if not binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers)):
    rI = min(list_sequence_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_sequence_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет введенного числа
Ближайшее меньшее число: {rI}, его индекс: {ind}
Ближайшее большее число: {list_sequence_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, его индекс: {list_sequence_numbers.index(rI)}
В списке нет меньшего числа''')
    elif rI > user_number:
        print(f'''В списке нет введенного числа
Ближайшее большее число: {rI}, его индекс: {list_sequence_numbers.index(rI)}
Ближайшее меньшее число: {list_sequence_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_sequence_numbers.index(rI) == 0:
        print(f'Индекс введенного числа: {list_sequence_numbers.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers))}')
