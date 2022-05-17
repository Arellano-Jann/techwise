def count_palindrome(word):
    split_string = word.split(" ")
    palindromes = [x for x in split_string if x == x[::-1]]
    return len(palindromes)

print(count_palindrome("aba abaa"))

# returns true if the second smallest number in the list is a fibonacci number
def fibonacci_sequence(num):
    a, b = 0, 1
    while b < num: # does <= cause a problem?
        yield b
        a, b = b, a+b

def is_sec_fib(list: [int]) -> bool:
    if len(list) < 2:
        return False
    list.sort()
    return list[1] in fibonacci_sequence(list[1]+1)

print(is_sec_fib([4, 8, 15, 16, 23, 42, 58, 89, 145, 233, 377, 610]))
print(is_sec_fib([13, 7 , 108, 12, 11, 9, 15]))