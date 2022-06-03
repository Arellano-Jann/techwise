def list2num(lst : [int]) -> int:
    num = 0
    print("In list:", lst)
    for i in lst[::-1]:
        num = num * 10 + i
    print("Out num:", num)
    return num

def num2list(num : int) -> [int]:
    print("In num:", num)
    string = str(num)
    lst = list(string)
    print("Out list:", lst)
    return [int(x) for x in lst]

def reverse_sum(lst : [int]) -> [int]:
    num = list2num(lst)
    num += 1
    newlst = num2list(num)
    return newlst[::-1]

print(reverse_sum([1,2,3]))
print()
print(reverse_sum([9,9,9]))
print()
print(reverse_sum([5,2,3,4,5]))

# longes palindromic substring # https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
def find_palindrome(start, end, string):
    if start < 0: # doesn't allow a negative start to prevent going to the end of the string
        return (0, end-1)
    if end >= len(string): # prevents out of bounds errors
        return (start+1, len(string)-1)
    if string[start] != string[end]: # a palindrome is a mirror. so start and end have to be the same character at all times or else...
        return (start+1, end-1)
    return find_palindrome(start-1, end+1, string) # recursive call to expand until it's no longer a palindrome (hits the base case)

def longest_palindrome(s: str):
    longest = s[0]
    for i in range(1, len(s)):
        # finds the palindrome if the string is odd (notice (i, i))
        start, end = find_palindrome(i, i, s)
        if (end - start + 1) > len(longest):
            longest = s[start : end+1]
        # finds the palindrome if the string is even (notice (i-1, i))
        start, end = find_palindrome(i-1, i, s)
        if (end - start + 1) > len(longest):
            longest = s[start : end+1]
    return longest

def longest_palindrome1line(string: str) -> str:
    return max([r for r in [t for y in [[string[i:u] for u in range(i + 1, len(string) + 1)] for i in range(len(string))] for t in y] if r == r[::-1]], key=len)
    # [[string[i:u] for u in range(i + 1, len(string) + 1)] for i in range(len(string))] # generates all substrings
    # [t for y in ... for t in y] # needed bc arr of strings is 2d array. therefore, it flattens to a 1d array




print(longest_palindrome1line("babad"))
print(longest_palindrome1line("cbbd"))
print(longest_palindrome1line("abcd"))
print(longest_palindrome1line("a"))
print(longest_palindrome1line("aba"))