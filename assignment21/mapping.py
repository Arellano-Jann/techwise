# higher order. mapping.
# ##Assignment - 21-01

# ###FizzBuzz Problem


# Write a function that prints the numbers in the given range but for multiples of **3** print **Fizz** and for multiples of **5** print **Buzz** and for multipes of **3 and 5** print **FizzBuzz**

def fizz_buzz(k: int)-> [str]:
    return list(map(lambda x: "FIZZBUZZ" if x % 15 == 0 else "FIZZ" if x % 3 == 0 else "BUZZ" if x % 5 == 0 else x, range(1, k+1)))

print(fizz_buzz(15))


# #Assignment - 21-02

# Write a Python program to list out the prime numbers in a given range.

# For Example:

# prime_sequence(20) => [2, 3, 5, 7, 11, 13, 17, 19]

# prime_sequence(30) => [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def prime_sequence(limit: int)-> [int]:
    # print(lambda x: all(x % i != 0 for i in range(2, x)), range(2, limit))
    x = 3
    print( all(x % i != 0 for i in range(2, x)) )
    return list(filter(lambda x: all(x % i != 0 for i in range(2, x)), range(2, limit)) ) # casts to int. filters for prime.
    # filter works by calling a lambda all in the range of the limit
    # all returns true if all elements in the iterable are true.
    # a list comprehension is called within all(). list contains numbers from 2 to the current number that is not divisible by the current index.
    # if all returns true, the number is added to the list. this is because filter works by true or false statements.

print(prime_sequence(20))


# #Assignment - 21-03

# ## Repeat Sequence Problem

# Implement a function to repeat the sequence as per the given order.

# Example

# repeat_sequence('ab') => A->Bb

# repeat_sequence('UVWX') => U->Vv->Www->Xxxx

def repeat_sequence(string: str) -> str:
    return "".join(map(lambda x: str(x).upper() + str(x*(string.index(x))).lower() + "->", string))

print(repeat_sequence('UVWX'))
print(repeat_sequence('ab'))