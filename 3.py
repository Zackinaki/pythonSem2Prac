# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

import math
import os
os.system('cls')

n = int(input("Vvdedite chislo: "))
x = 1

if n > 0:
    print(2**0)
while x < n:
    if (x <= n):
        if (x * 2 > n):
            break
        else:
            x = x * 2
            print(x)
