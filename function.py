import random

#функции

def create_random_int_number_list(len_list):
    numbers = [random.randint(1, 10) for _ in range(len_list)]
    return numbers

result = create_random_int_number_list(5)
print(result)


# сослучайным количеством результата
def create_random_int_number_list(len_list=5):  # длина всегда будет 5
    numbers = [random.randint(1, 10) for _ in range(len_list)]
    return numbers

len_list = random.randint(10, 20)
result = create_random_int_number_list(len_list)
print(result)


########
def print_dict(some_dict):   # все что используем, передаем в функцию!!!!!
    for key, value in some_dict.items():
        print(f'{key}: {value}')


my_dict = {'val_1': 12, 'val_2': 24, 'val_3': 6, 'val_4': 58}

person = {'name': 'John',
          'age': '23',
          'sex': 'Male',
          'address': {'city': 'Dnipro',
                      'street': 'Polya',
                      "ZIP": 49000
                      },
          'skils': {'hard': ['python', 'html', 'DB', 'C++'],
                    'soft': []
                    }
          }
# print(person)
# print_dict(person)
# print_dict(some_dict=my_dict)


########################################################

def hello():
    print("Hello, World!")

hello()
hello()
hello()

# x = int(input('Number_1: '))
# y = int(input('Number_2: '))
#
# def sum(a, b):
#     return a + b
#
# z = sum(x, y)
# print(z)

###
def f(a):
    return  2 * a - 2

print(f(2))

######################################
def hello(name):
    if len(name) > 4:
        print('Hello, ' + name)
    else:
        print('You have shirt name, ' + name)
hello('Alice')
hello('Bob')

####
def hello(len_name):
    print(len(len_name))
hello('Alice')
hello('Bob')

############

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)


# обработка исключений

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


########### угадай число ##########
import random

secretNumber = random.randint(1, 20)
print('Задумано число от 1 до 20. Попробуй угадать его')
# предоставить игроку 6 попыток угадать
for guessesTaken in range(1, 7):
    print('Ваш вариант: ')
    guess = int(input())
    if guess < secretNumber:
        print('Попробуй больше')
    elif guess > secretNumber:
        print('Попробуй меньше')
    else:
        break

if guess == secretNumber:
    print('Верно! Количество попыток: ' + str(guessesTaken))
else:
    print('Нет! Было задуманно число: ' + str(secretNumber))
