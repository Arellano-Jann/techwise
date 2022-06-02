# finds the first non repeating character in it and return its index. if it doesnt exist, return -1
def first_uniq_char(s: str) -> int:
    for i in s:
        if s.count(i) == 1: # finds the first element that only has a count of one, and is therefore unique in the string
            return s.index(i)
    return -1 # returns -1 if no unique elements are found



print(first_uniq_char("lovecoding"))
print(first_uniq_char("abcd"))
print(first_uniq_char("tattletale"))
print(first_uniq_char("aaabbc"))