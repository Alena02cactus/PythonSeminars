<!-- здесь я буду сохранять условия задач (которые не успела решить) и разные подсказки для кода -->





Кортеж — это неизменяемый список.
Словари — неупорядоченные коллекции произвольных объектов с доступом по
ключу.
Список - это упорядоченный конечный набор элементов. Давайте разбираться, по
сути список - это тот же самый массив, в котором можно хранить элементы любых
типов данных.

Как работать со списками?
list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка 
list_1 = [7, 9, 11, 13, 15, 17]

Чтобы узнать количество элементов в списке необходимо использовать функцию
len(имя_списка):
list_1 = [7, 9, 11, 13, 15, 17]
print(len(list_1)) # 6

Можно список заполнять не только при его создание, но и во время работы
программы:

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
n = int(input()) # пользователь вводит целое число
list_1.append(n) # сохранение элемента в конец списка
<!-- # 1-я итерация цикла(повторение 1): n = 12, list_1 = [ 12 ]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0] -->
print(list_1) # [12, 7, -1, 21, 0]

