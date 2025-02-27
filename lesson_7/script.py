# Задание 1
with open(file='data.txt', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line)

# Задание 2
name = str(input('Введите имя:'))
age = input('Введите возраст:')
with open(file='userinfo.txt', mode='a+') as file:
    file.write(f'{name}:{age}\n')

# Задание 3

with open(file='copy.txt', mode='a+') as file_copy:
    with open(file='original.txt', mode='r') as file_original:
        for line in file_original.readlines():
            file_copy.write(line)