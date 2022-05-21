from math import factorial


import math

def is_strongnumber(num):
    string = str(num)
    return sum([math.factorial(int(x)) for x in string]) == num

print(is_strongnumber(145))

def min_val(lst):
    return min(lst) * -1 + 1 if min(lst) < 1 else 0