# filter
# #Assignment - 22 - 01

# ##Euler Problem-2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib_sequence(limit):
    a, b = 0, 1
    while b < limit: # while limit hasn't been reached
        yield b # add b to a collection. yield adds to a collection without stopping
        a, b = b, a+b # generate new values
        # we don't care about the 0 and 1 values really because they are not even

def euler2(limit: int)-> int:
    return sum(filter(lambda x: x % 2 == 0, fib_sequence(limit))) # in the fib sequence, it sums all even numbers filtered by the lambda filter.

print(list(fib_sequence(400)))
print(euler2(4000000))


# #Assignment - 22 - 02

# Generate the Amstrong numbers between two given numbers.

# Example: 

# make_armstrong(100, 1000) => [153, 370, 371, 407]

def is_armstrong(num):
    # could also convert to num inside function instead of outside
    num = str(num)
    return sum(int(x)**3 for x in num) == int(num)

def make_armstrong(start: int, limit: int)-> [int]:
    return list(filter(is_armstrong, range(start, limit)))
    # return list(filter(is_armstrong, map(str, range(start, limit)))) # need to do this if not converting to string inside the function. map is cool

print(is_armstrong("370"))
print(make_armstrong(100, 1000))


# #Assignment - 22- 03

# Write a function that classifies given list of numbers into **Even** and **Odd** Sublists.

# split_even_odd_sublist([2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 12, 14, 15, 21]) => ([2, 4, 6, 8, 12, 14], [1, 3, 5, 7, 9, 11, 15, 21])

def split_even_odd_sublist(num_list: [int]) -> ([int], [int]):
    return (list(filter(lambda x: x % 2 == 0, num_list)), list(filter(lambda x: x % 2 == 1, num_list)))

print(split_even_odd_sublist([2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 12, 14, 15, 21]))