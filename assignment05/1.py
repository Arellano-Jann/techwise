# Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

# Of course we do not want to sprinkle print statements, so let us generate them.

def fizz_buzz(n: int)-> list(str):
    #Write your code here
    fizzbuzz = []
    for x in range(1, n):
        if (x%3==0) and (x%5==0):
            fizzbuzz.append("FizzBuzz")
        if (x%3==0):
            fizzbuzz.append("Fizz")
        if (x%5==0):
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(x)
    return fizzbuzz

# Write a function that Converts vowels into upper case character and consonants into lower case character in a given string .
def vowel_to_upper_cons_to_lower(string: str)-> str:
    #Write your code here
    vowels = "aeiou"
    newString = ""
    for x in str:
        if x in vowels:
            x.upper()
            newString += x
        else:
            x.lower()
            newString += x
    return newString

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
    return 