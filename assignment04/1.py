# Take any four-digit number, using at least two different digits (leading zeros are allowed). Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary. Subtract the smaller number from the bigger number. Go back to step 2 and repeat. This process stops after a few steps, that is step 3 produces the same number. DO this with paper and pen to understand the same Start with  1945 
# 9541–1459=8082 
# 8820–0288=8532 
# 8532–2358=6174 
# 7641–1467=6174 
# Given a suitable starting number generate the sequence, stopping the output without any repetition.
# For example if 1945 is input it should return  [1945,8082,8532,6174]

def kaprekar_seq(n: int) -> [int]:
    #Write your code here
    
    numbers = []
    first_number = 
    second_number = 
    new_number = first_number - second_number
    if new_number == numbers(len(numbers) - 1):
		return numbers
    else:
        numbers.append(new_number)
        kaprekar_seq(new_number)  ## might work??

# Start with any number. (For practice try small numbers) say 7
# if it is even divide by 2, if it is odd multiply by 3 and add 1
# Repeat
# This process reaches at ...4, 2, 1 and then starts repeating
# Write a function that generates the sequence ending in 4, 2, 1 for the given starting number
# For example  7  should generate  [7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]

def collatz_sequence(k: int) -> [int]:
    #Write your code here
    
    return 