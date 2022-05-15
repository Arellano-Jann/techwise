# ##Assignment - 19-01

# Write one function to calculate the perimeter of triangle, rectangle, pentagone, hexagone.

def perimeter_of_shape(*sides)->int:
  #write your code here
  return sum(sides)

print(perimeter_of_shape(1,2,3))


# #Assignment - 19 - 02

# Implement a function which take multiple strings as input. Concatenate the strings in the reverse order after reversing the strings.

# Examples:
# > display_in_reverse_order("Hello", "Good", "Morning") --> 'gninroMdooGolleH'

def display_in_reverse_order(*strings):
    #Write your code here
    final = ""
    for x in strings[::-1]:
        final += x[::-1]
    return final

print(display_in_reverse_order("Hello", "Good", "Morning"))