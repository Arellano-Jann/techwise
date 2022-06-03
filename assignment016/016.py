# finds the first non repeating character in it and return its index. if it doesnt exist, return -1
def first_uniq_char(s: str) -> int:
    for i in s:
        if s.count(i) == 1: # finds the first element that only has a count of one, and is therefore unique in the string
            return s.index(i)
    return -1 # returns -1 if no unique elements are found



print(first_uniq_char("lovecoding"))
print(first_uniq_char("abcd"))
print(first_uniq_char("tattletale"))
print(first_uniq_char("aaabbc"))

# write a function that takes a list of distinct integers as input and returns True if the second largest number is a prime number and returns False otherwise

def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0: # checks if the num is perfectly divisible
            return False # returns false because the number cannot be divisible by ANY number 
    return True


def is_sec_prime(lst: [int]) -> bool:
    lst.sort()
    return is_prime(lst[-2]) if len(lst) > 2 else is_prime(lst[0]) if len(lst) == 1 else False

def is_sec_prime1line(lst: [int])-> bool:
    return (all([sorted(list(set(lst)))[-2] % i for i in range(2, sorted(list(set(lst)))[-2])]) if sorted(list(set(lst)))[-2] > 1 else False) if len(sorted(list(set(lst)))) > 1 else False


print (is_sec_prime([5,6]))
print (is_sec_prime([5,8]))
print (is_sec_prime([10,8,12]))
print (is_sec_prime([5,8,7]))
print (is_sec_prime([]))
print (is_sec_prime([5]))