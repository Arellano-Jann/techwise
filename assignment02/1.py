# If the sum of the proper divisors of a number is equal to the number itself, it is called a perfect number. Examples: 6 and 28

# If the sum of the proper divisors of the number is greater than the number itself, we call the number an abundant number. Example: 12

# If the sum of the proper divisors of the number is less than the number itself, we call the number a deficient number. Example: all primes, all powers of 2

# Write a function that classifies a number as above. It should return 0 if the argument is perfect, -1 if deficient and +1 if abundant


def classify(k: int) -> int:
    divisor_sum = 0
    for x in range(1, k//2+1):
        if (k % x == 0):
            divisor_sum += x
    if divisor_sum > k:
        return 1
    if divisor_sum < k:
        return -1
    if divisor_sum == k:
        return 0
    
print(classify(6))
print(classify(28))
print(classify(12))
print(classify(7))


# Write a function that determines the number of digits in an integer
def num_digits(p: int) -> int:
    digit_count = 0
    while p > 0:
        p //= 10
        digit_count +=1
    return digit_count

print(num_digits(6))
print(num_digits(98946))
print(num_digits(66))

# A three digit number is called Armstrong, if it is equual to the sum of the cubes of its digits:

# Example:  156=13+53+63=1+125+216=342≠156  is NOT an Armstrong number

# But  153=13+53+33=1+125+27=153  is an Armstrong number.

# Write a function to check if a given three digit number is Armstrong

def is_armstrong(n: int) -> bool:
    # Write code here
    cube_sum = 0
    armstrong = n
    while n > 0:
        ones_place = n % 10
        cube_sum += (ones_place ** 3)
        n //= 10
    return cube_sum == armstrong

print(is_armstrong(156))
print(is_armstrong(153))