#  Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)



import random

list=[random.randint(-50, 50) for i in range(random.randint(10,20))]

print(list)
min=int(input("введите минимальное число диапазона : "))
max=int(input("введите максимальное число диапазона : "))

masi=[]

if max >= min:

   for i in range(len(list)):

      if max >= list[i] and min <= list[i]:

          masi.append(i)

   print("Кол-во:",len(masi))

   print("Индексы:",masi)


