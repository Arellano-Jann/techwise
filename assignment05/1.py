# Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

# Of course we do not want to sprinkle print statements, so let us generate them.

def fizz_buzz(n: int)-> [str]:
    #Write your code here
    fizzbuzz = []
    for x in range(1, n+1):
        if (x % 3 == 0) and (x % 5 == 0):
            fizzbuzz.append("FizzBuzz")
        elif (x % 3 == 0):
            fizzbuzz.append("Fizz")
        elif (x % 5 == 0):
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(x)
    return fizzbuzz

print(fizz_buzz(16))



# Write a function that Converts vowels into upper case character and consonants into lower case character in a given string .
def vowel_to_upper_cons_to_lower(string: str)-> str:
    #Write your code here
    string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    newString = ""
    for x in string:
        if x in vowels:
            newString += x.upper()
        else:
            newString += x.lower()
    return newString

print(vowel_to_upper_cons_to_lower("HaiShifu"))


# Write a function that classifies given list of numbers into Even and Odd Sublists.
def split_Even_Odd_Sublist(num_array):
    #Write your code here
    odd_list = []
    even_list = []
    for x in num_array:
        if x%2==0:
            even_list.append(x)
        else:
            odd_list.append(x)
    return odd_list, even_list


arr = [1,3,5,2,3,68,9,2,1]
print(split_Even_Odd_Sublist(arr))