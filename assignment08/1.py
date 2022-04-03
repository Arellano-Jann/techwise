# Pascal's triangle
#           1
#        1     1
#      1    2    1
#    1   3     3   1
#  1   4     6    4   1 
# The triangle can be constructed by first placing a 1 along the left and right edges. Then the triangle can be filled out from the top by adding together the two numbers just above to the left and right of each position in the triangle. Thus, the third row, in Hindu-Arabic numerals, is 1 2 1, the fourth row is 1 4 6 4 1, the fifth row is 1 5 10 10 5 1, and so forth. The first row, or just 1, gives the coefficient for the expansion of (x+y)0=1; the second row, or 1 1, gives the coefficients for (x+y)1=x+y; the third row, or 1 2 1, gives the coefficients for (x+y)2=x2+2xy+y2; and so forth.

from math import factorial

def pascal_output(size: int) -> str:
    pascal_array = []
    for x in range(size):
        print(upto_n(x))
    return 




# Printing patterns
# Given a number  n  generate the following pattern

# 1

# 2 3

# 4 5 6

# 7 8 9 10

# 11 12 13 14 15

# ... n

# **

# where  n  is the last number. Note that this means

# the last line has just two stars
# the penultimate line may not be longer than the previous line.
# The triangle can be constructed by first placing a 1 along the left and right edges. Then the triangle can be filled out from the top by adding together the two numbers just above to the left and right of each position in the triangle. Thus, the third row, in Hindu-Arabic numerals, is 1 2 1, the fourth row is 1 4 6 4 1, the fifth row is 1 5 10 10 5 1, and so forth. The first row, or just 1, gives the coefficient for the expansion of (x+y)0=1; the second row, or 1 1, gives the coefficients for (x+y)1=x+y; the third row, or 1 2 1, gives the coefficients for (x+y)2=x2+2xy+y2; and so forth.

def upto_n(n: int) -> str:
    #Write your code Here
    return 