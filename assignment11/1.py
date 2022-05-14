# Implement a function that converts roman number to arabic number

# Example:

# roman2arabic("V") --> 5

# roman2arabic("IX") --> 9

def roman2arabic(r: str) -> int:
    #Write your code Here
    roman_dictionary = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000 }
    r = r.upper()
    total = 0
    
    r = r.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC") # sets to a standard format
    for i in r:
        total += roman_dictionary[i]
    return total

print(roman2arabic("V"))
print(roman2arabic("IX"))
print(roman2arabic("XC"))
print(roman2arabic("CM"))
print(roman2arabic("MMMCMXCIX"))

# program to convert arabic to roman

# Example:

# arabic2roman(5) --> V

# arabic2roman(9) --> IX

def arabic2roman(num:int) -> str:
    #Write your code Here
    if num > 3999:
        return "Number is too large"
    roman_dictionary = {
                        "M": 1000,
                        "CM": 900,
                        "D": 500,
                        "CD": 400,
                        "C": 100,
                        "XC": 90,
                        "L": 50,
                        "XL": 40,
                        "X": 10,
                        "IX": 9,
                        "V": 5,
                        "IV": 4,
                        "I": 1
                        }
    roman = ""
    for keys in roman_dictionary:
        while num >= roman_dictionary[keys]:
            roman += keys
            num -= roman_dictionary[keys]
    return roman

print(arabic2roman(5))
print(arabic2roman(9))
print(arabic2roman(10))
print(arabic2roman(11))
print(arabic2roman(12))
print(arabic2roman(13))
print(arabic2roman(22))
print(arabic2roman(23))
print(arabic2roman(24))
print(arabic2roman(25))
print(arabic2roman(26))
print(arabic2roman(37))
print(arabic2roman(38))
print(arabic2roman(39))
print(arabic2roman(40))
print(arabic2roman(41))
print(arabic2roman(48))
print(arabic2roman(49))
print(arabic2roman(50))
print(arabic2roman(51))
print(arabic2roman(52))
print(arabic2roman(53))
print(arabic2roman(5004))
print(arabic2roman(3999))