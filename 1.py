# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# 2

import os
os.system('cls')

n = int(input("Vvdedite kol-vo monet: "))
sum_tails = 0
sum_eagle = 0

print("Vvdeite polozhenie vseh monet: ")
for i in range(n):
    status = int(input())
    if status > 0:
        sum_eagle += 1
    else:
        sum_tails += 1
if sum_eagle > sum_tails:
    print("Minimal'noe kol-vo monet dla perevorachivania:", sum_tails)
else:
    print("Minimal'noe kol-vo monet dla perevorachivania:", sum_eagle)
