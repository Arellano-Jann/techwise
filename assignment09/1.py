# Write a program that produces a tableau like this

#  13  17 + 

#   6  34 × 

#   3  68 + 

#   1 136 + 

# =221 

# Remember that the algorithm is : Halve and double; Add the  + s, skip the  × s. The purpose is to also do a bit of output formatting
#  the  × s are rows that have left side even

def rus_mult_print(a: int, b: int) -> None:
    #Write your code Here
    if a % 2 == 0:
        print(a, b, "×")
        return rus_mult_print(a // 2, b*2)
    if a == 1:
        print(a, b, "+")
        return b
    print(a, b, "+")
    # print("=", b)
    return b + rus_mult_print(a // 2, b*2)

print(rus_mult_print(13, 17))