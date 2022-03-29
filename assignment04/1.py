# Take any four-digit number, using at least two different digits (leading zeros are allowed). Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary. Subtract the smaller number from the bigger number. Go back to step 2 and repeat. This process stops after a few steps, that is step 3 produces the same number. DO this with paper and pen to understand the same Start with  1945 
# 9541–1459=8082 
# 8820–0288=8532 
# 8532–2358=6174 
# 7641–1467=6174 
# Given a suitable starting number generate the sequence, stopping the output without any repetition.
# For example if 1945 is input it should return  [1945,8082,8532,6174]

def rotate_number(n):
    n *= 10
    num_array = str(n)
    size_of_array = len(num_array)
    num_array[size_of_array] = num_array[0]
    num_array = num_array[1:]
    return int(num_array)

def reverse_number(n):
    num_array = str(n)
    # num_array[::-1]
    num_array.reverse()
    return int(num_array)


def kaprekar_seq(n: int) -> [int]:
    #Write your code here
    while True:
      	numbers = [n]
		first_number = rotate_number(n)
		second_number = reverse_number(first_number)
		new_number = first_number - second_number
		if new_number == numbers(len(numbers) - 1):
			return numbers
		else:
			numbers.append(new_number)

# Start with any number. (For practice try small numbers) say 7
# if it is even divide by 2, if it is odd multiply by 3 and add 1
# Repeat
# This process reaches at ...4, 2, 1 and then starts repeating
# Write a function that generates the sequence ending in 4, 2, 1 for the given starting number
# For example  7  should generate  [7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1]

def collatz_sequence(k: int) -> [int]:
    #Write your code here
	numbers = []
    while True:
		numbers.append(k)
		if (k%2==0):
			k //= 2
		else if k==1:
			return numbers
		else:
			k *= 3
			k += 1

    return numbers