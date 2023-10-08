############################################
# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.
import string

persons = [
    {"name": "John", "age": 15},
    {"name": "Michael", "age": 17},
    {"name": "Adam", "age": 42},
    {"name": "Jil", "age": 18},
    {"name": "Lina", "age": 32},
    {"name": "Aaron", "age": 25},
    {"name": "Noa", "age": 15},
    {"name": "Jack", "age": 55}
]

# а) Напечатать имя самого молодого человека.
# Если возраст совпадает - напечатать все имена самых молодых.

min_age_person = []
min_age = 1500
longest_name = 0
sum_age = 0

for person in persons:
    if person["age"] < min_age:
        min_age = person["age"]

for person in persons:
    if person["age"] == min_age:
        min_age_person.append(person["name"])
print(min_age_person)

# б) Напечатать самое длинное имя.
# Если длина имени совпадает - напечатать все имена.

longest_name_list = []
for person in persons:
    if len(person["name"]) > longest_name:
        longest_name = len(person["name"])

for person in persons:
    if len(person["name"]) == longest_name:
        longest_name_list.append(person["name"])
print(longest_name_list)

# в) Посчитать среднее количество лет всех людей из списка.

for person in persons:
    sum_age += person["age"]
middle_age = sum_age/len(persons)
print(middle_age)

############################################
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом,
# но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря,
# значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные
# в предыдущих пунктах.

my_dict_1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
my_dict_2 = {'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'one': 5, 'ten': 10, 'five': 6}

# а) Создать список из ключей, которые есть в обоих словарях.

my_dict_1_set = set(my_dict_1)
my_dict_2_set = set(my_dict_2)

new_dict = list(my_dict_1_set.intersection(my_dict_2_set))
print(new_dict)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

new_dict_2 = list(my_dict_1_set.difference(my_dict_2_set))
print(new_dict_2)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом,
# но нет во втором словаре.

# my_dict_3 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
# print(my_dict_3, type(my_dict_3))

my_dict_3 = dict()
for key in my_dict_1:
    if key not in my_dict_2:
        my_dict_3[key] = my_dict_1[key]
print(my_dict_3, type(my_dict_3))

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря,
# значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные
# в предыдущих пунктах.

my_dict_4 = {}
for key in my_dict_1:
    if key not in my_dict_2:
        my_dict_4[key] = my_dict_1[key]
    elif key in my_dict_2:
        my_dict_4[key] = [my_dict_1[key], my_dict_2[key]]
for key_2 in my_dict_2:
    if key_2 not in my_dict_1:
        my_dict_4[key_2] = my_dict_2[key_2]
print(my_dict_4)

######################################
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ['name', 'couple', 'family', 'God', 'love', 'hope']
def my_function(my_list):
    new_list = []
    for index in my_list:
        if index in my_list[1::2]:
            new_list.append(index[::-1])
        else:
            new_list.append(index)
    return new_list

new_list = my_function(my_list)
print(new_list)

######################################
# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com


import random
from string import ascii_lowercase

def create_email(domains, names):
  return random.choice(names) + '.' \
         + str(random.randint(100, 1000)) \
         + '@' \
         + ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7))) \
         + '.' \
         + random.choice(domains)

names = ['king', 'miller', 'kean', 'jons', 'demin', 'lord']
domains = ["net", "com", "ua", 'org']
e_mail = create_email(domains, names)
print(e_mail)