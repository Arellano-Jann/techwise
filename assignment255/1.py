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
def is_palindrome(s : str) -> bool:
    return s == s[::-1]

def longest_palindrome(s : str) -> str:
    if is_palindrome(s):
        return s
    long1 = longest_palindrome(s[1:])
    long2 = longest_palindrome(s[:-1])
    return long1 if long1 > long2 else long2

def longest_palindrome1line(string: str) -> str:
    return max([r for r in [t for y in [[string[i:u] for u in range(i + 1, len(string) + 1)] for i in range(len(string))] for t in y] if r == r[::-1]], key=len)
    # [[string[i:u] for u in range(i + 1, len(string) + 1)] for i in range(len(string))] # generates all substrings
    # [t for y in ... for t in y] # needed bc arr of strings is 2d array. therefore, it flattens to a 1d array

def is_sec_prime1line(lst: [int])-> bool:
    return (all([sorted(list(set(lst)))[-2] % i for i in range(2, sorted(list(set(lst)))[-2])]) if sorted(list(set(lst)))[-2] > 1 else False) if len(sorted(list(set(lst)))) > 1 else False


print(longest_palindrome1line("babad"))
print(longest_palindrome1line("cbbd"))
print(longest_palindrome1line("abcd"))
print(longest_palindrome1line("a"))
print(longest_palindrome1line("aba"))