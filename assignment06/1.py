# Built-in Function len()
# *Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection *

# Problem Statement
# Implement a function which accepts a sequence as an argument and returns the length of the sequence or a collection.

# Example:
# > length("Hello") --> 5

# > length([]) --> 0

# > length((1, 2, 3, 4, 5)) --> 5

def length(seq) -> int:
    if not seq:
        return 0
    else:
        return 1 + length(seq[1:])

print(length("Hello"))
print(length([]))
print(length((1, 2, 3, 4, 5)))



# Built-in Function sum()
# Sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

# Problem Statement
# Implement a function which accepts an iterable as an argument and returns the total

# Note: The iterable’s items are normally numbers. Strings are not considered
# Example:
# > summation([1, 2, 3, 4, 5]) --> 15

# > summation([0]) --> 0

# > summation([]) --> 0

# > summation((1, 2, 3, 4, 5)) --> 15

def summation(seq) -> int:
    #Write your code here
    if not seq:
        return 0
    else:
        return seq[0] + summation(seq[1:]) 

print(summation([1, 2, 3, 4, 5]))
print(summation([0]))
print(summation([]))
print(summation((1, 2, 3, 4, 5)))

# Take any four-digit number, using at least two different digits (leading zeros are allowed). Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary. Subtract the smaller number from the bigger number. Go back to step 2 and repeat. This process stops after a few steps, that is step 3 produces the same number. DO this with paper and pen to understand the same Start with  1945 

# 9541–1459=8082 

# 8820–0288=8532 

# 8532–2358=6174 

# 7641–1467=6174 

# Given a suitable starting number generate the sequence. It should not repeat; that is it should stop before the repetition.

# For example if 1945 is input it should return [1945,8082,8532,6174]

def tiny_num(n):
    num = n
    num_array = sorted(str(num))
    new_string = "".join(num_array)
    # print(int(new_string), "tiny", n)
    return int(new_string)


def big_num(n):
    num = n
    num_array = sorted(str(num), reverse = True)
    new_string = "".join(num_array)
    # print(int(new_string), "big", n)
    return int(new_string)

def kaprekar_subtraction(n: int):
    #Write your code here
    first_number = tiny_num(n)
    second_number = big_num(n)
    new_number = second_number - first_number
    # print(new_number, "nn", n)
    return new_number


def kaprekar_seq(n: int) -> [int]:
    #Write your code here
    kap_num = kaprekar_subtraction(n)
    if n == kap_num:
        return [n]
    else:
        # print("new seq")
        return [n] + kaprekar_seq(kap_num)
    
print(kaprekar_seq(1945))