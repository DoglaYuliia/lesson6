################ ГЕНЕРИРОВАНИЕ ЧИСЕЛ ################

# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.

import random         # импорт всего модуля
# from random import randint   # испорт конкрутной функцмм

from string import ascii_lowercase as alphabet

alphabet_list = list(alphabet)
print(alphabet_list, type(alphabet_list))

random.shuffle(list(alphabet_list))
print(alphabet_list)

####
value = random.randint(1, 10)
print(value)


#
# random.choice(sequence) - случайный элемент непустой последовательности.
# случайный выбор из списка
my_list = ['True', 'False', 'Unknown']
my_choice = random.choice(my_list)
print(my_choice)


# random.shuffle(sequence, [rand]) - перемешивает последовательность (изменяется сама последовательность).
# Поэтому функция не работает для неизменяемых объектов.

random.shuffle(my_list)
print(my_list)
