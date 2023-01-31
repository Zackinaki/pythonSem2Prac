# 2. Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница. Петя помогает Кате по математике.
#  Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
#  Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

import math
import os
os.system('cls')

s = int(input("Vvdedite summu chisel: "))
p = int(input("Vvdedite proizvedenie chisel: "))
x = 0

for x in range(1000):
    x = int((s-math.sqrt(s**2-4*p))/2)

y = s-x

print("Pervoe chislo ranvo", x, "\nVtoroe chislo ranvo", y)
