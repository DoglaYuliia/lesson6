# Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# Их иногда ещё называют ассоциативными массивами или хеш-таблицами.

# пара - ключ: значение
# ключами может быть любой неизменяемый тип данных или позьзовательский тип
my_dict = {'name': 'John', 'age': '23', 1: 11}  # изменяемый, итерируемый тип данных. Порядок ключей не гарантируются.

# print(my_dict, type(my_dict))

print(my_dict['name'])

print(my_dict.get('name'))
print(my_dict.get(111))  #не выдает ошибку

#добавить в словарь
person = {'name': 'John', 'age': '23'}
person['sex'] = 'Male'
print(person)

#или
person.update({'sex': 'Male'})
#print(person)

#влить один словарь в другой

person_details = {'sex': 'Male', 'address': 'Dnipro'}
person.update(person_details)
print(person)

# можно перезаписать ошибочное значение по ключу словаря
# метод update обновляет текущий словарь

#если мне нужен новый словарь
person = {'name': 'John', 'age': '23'}
person_details = {'sex': 'Male', 'address': 'Dnipro'}

new_person = dict()
new_person.update(person)
new_person.update(person_details)
#print(new_person)
# или в новой версии
new_person = person | person_details
print(new_person)

# или магия того же самого; распаковка словарей и объединение словарей в новый словарь
new_person = {**person, **person_details}

#приведение типов, из кортежа или списка с внутренней структурой в два элемента делается словарь
my_tuple = (('name', 'John'), ('age', 23))
my_list_1 = [['name', 'John'], ['age', 23]]
my_list_2 = [('name', 'John'), ('age', 23)]

person = dict(my_tuple)
person_2 = dict(my_list_1)
person_3 = dict(my_list_2)
print(person, type(person))
print(person_2, type(person_2))
print(person_3, type(person_3))

#####

#внутри словаря другой словарь, кот лежит за соответствующим ключем
address = {'city': 'Dnipro', 'street': 'Polya', "ZIP": 49000}

person = {'name': 'John', 'age': '23'}
person_details = {'sex': 'Male', 'address': address}

new_person_2 = {**person, **person_details}
print(new_person_2)
print(new_person_2['address']['city'])

###
address = {'city': 'Dnipro', 'street': 'Polya', "ZIP": 49000}
skils = {'hard': ['python', 'html', 'DB', 'C++'], 'soft': []}
person = {'name': 'John', 'age': '23', 'skils': skils}
person_details = {'sex': 'Male', 'address': address}
new_person = {**person, **person_details}
new_person['skils']['hard'].append('JS')
print(new_person)

### по-хорошему, хороший тон записи словаря

person = {'name': 'John',
          'age': '23',
          'skils': {'hard': ['python', 'html', 'DB', 'C++'],
                    'soft': []
                    },
          'sex': 'Male',
          'address': {'city': 'Dnipro',
                      'street': 'Polya',
                      "ZIP": 49000
                      }
          }

#######
my_dict = {1: 11, (1, 2, 3): 'test', '1': 'TEST'}
# можем делать проверку
print('1' in my_dict)  # in смотрит только на ключей


################ три важные МЕТОДЫ словарей

print(my_dict.keys())  #- создает кейс, объект, где только ключи
# dict_keys - 'почти' список ключей
keys = list(my_dict.keys())

values = my_dict.values()
print(values)   # 'почти' список значений

for value in values:    # лучше 'одевать' на него list
    print(values)

items = my_dict.items()  # получается список кортежей
print(items)

# цикл for 'идет' только ПО КЛЮЧАМ
for key in my_dict:
    print(key, my_dict[key])  # для значений отдельно

# если нужны только одни значения

my_dict = {'val_1': 12, 'val_2': 24, 'val_3': 6, 'val_4': 58}
res_value = []
for value in my_dict.values():
    if value > 10:
        res_value.append(value)
print(res_value)

# и keys
res_value = []
res_keys = []
for key, value in my_dict.items():
    if value > 10:
        res_value.append(value)
        res_keys.append(key)
print(res_value)
print(res_keys)


#сгенерировать словарь
my_temp_dict = {11: 1, 12: 2, 13:3}
print(my_temp_dict)
if len(my_temp_dict.values()) == len(set(my_temp_dict.values())):  # проверка на уникальность значений
    temp_revers_dict = {value: key for key, value in my_temp_dict.items()}
# тут разрываем словарь на пары и как-бы меняем значение и ключ местами,
# но только если значения уникальны
    print(my_temp_dict)




##############################################





