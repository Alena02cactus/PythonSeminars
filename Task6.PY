# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

number = int(input('введите номер билета '))
sum1 = int 
sum2 = int
sum1 = number//1000
sum2 = number%1000
sum1 = sum1//100 + (sum1//10 - sum1//100*10) + sum1%10
sum2 = sum2//100 + (sum2//10 - sum2//100*10) + sum2%10
if sum1 == sum2 :
    print ('yes')
else:
    print('no')

