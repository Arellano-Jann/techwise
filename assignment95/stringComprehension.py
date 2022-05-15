def is_same(string):
    vowels = "AEIOUaeiou"
    return len("".join([x for x in string if x in vowels])) == len("".join([x for x in string if x.isalpha() and x not in vowels]))

print(is_same("abeg"))
print(is_same("abeg@!#"))
print(is_same("abe"))
print()

def is_part_of_integer(lst: [int], n):
    string = str(n)
    return len([x for x in string if int(x) in lst]) == len(string)

print(is_part_of_integer([1,2,3], 123))
print(is_part_of_integer([1,2,3], 1234))
print(is_part_of_integer([1,2,3], 456))
print(is_part_of_integer([1,2,3,4], 123))