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
    
print(longest_palindrome1line("babad"))
print(longest_palindrome1line("cbbd"))
print(longest_palindrome1line("abcd"))
print(longest_palindrome1line("a"))
print(longest_palindrome1line("aba"))