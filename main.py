from array import array
from asyncio.windows_events import NULL
from pickle import NONE, TRUE #задача 1
import random #задача 2
from turtle import back #задача 1

 ##Первая задача:
 ##На столе лежат n монеток.
 ##Некоторые из них лежат вверх решкой, а некоторые – гербом. 
 ##Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
 ##Выведите минимальное количество монет, которые нужно перевернуть

 #n = 0
 #coin = 0
 #n = int(input())

 #arr = array.array('i')

 #arr = [random.randint(0, 1) for i in range(n)]

 #for i in arr: 
 #    if(i == 0):
 #        coin += 1


 #print(arr)
 #print("требуется ", coin,  "перевертышей")





## Вторая задача 
## Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
## Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
## Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
## Помогите Кате отгадать задуманные Петей числа.

#x = 0
#y = 0
#max_value = 1000
#temp = 0
#sum_xy = 0
#multisum = 0
#index = max_value / 2
 
#x = random.randint(1, max_value)
#y = random.randint(1, max_value)

#sum_xy = x + y
#multisum = x * y
#print(sum_xy, multisum)

#while TRUE:
#    if (int(index) > x):
#        temp = int(index)
#        index = int(index) / 2
#        max_value = int(temp)
#    elif (int(index) < x):
#        index = (int(index) + max_value) / 2
#    else:
#        break

#print("Первое число = ", x, "\nВторое число = ", int(multisum / x))





##Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.


#value = 0
#index = 0

#print("Введите число:", )
#n = int(input())

#while(index <= n):
#    value = 2 ** index
#    print(value)
#    index += 1

