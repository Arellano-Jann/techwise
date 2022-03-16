def best_of_3(a: int, b: int, c: int) -> int:
    # Write code here
    return a if a > b > c else b if b > c else c

def two_out_of3(a: bool, b: bool, c: bool) -> bool: 
    return not (a ^ b ^ c)
    # return False if a and b and c else True if a and b else True if b and c else True if a and c else False
    
# def to_array(number: int):
#     # Returns numbers reverse
    
#     return
 

def is_palindrome(number):
    temp = number
    reverse = 0
    while (temp > 0):
        reverse = (reverse * 10) + temp % 10
        temp //= 10
    return reverse == number
   
def next_palindrome(a: int) -> int:
    while (True):
        if (is_palindrome(a)):
            return a
        else:
            a += 1
    return 0

print(next_palindrome(10))
print(next_palindrome(1001))
print(next_palindrome(1100))
print(next_palindrome(1111))
print(next_palindrome(1234))


# print(two_out_of3(True,False,True))
# print(two_out_of3(False,True,True))
# print(two_out_of3(True,True,False))
# print(two_out_of3(False,True,False))
# print(two_out_of3(True,True,True))
# print(two_out_of3(False,False,True))
# print(two_out_of3(True,False,False))
