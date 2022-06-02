# happy number

def num2list(num):
    return [x for x in str(num)]
    
def is_happy_helper(n): # returns the sum of all digits to the second power
    lst = num2list(n)
    num = 0
    for val in lst:
        num += (int(val) ** 2)
    return num
    

def is_happy(n: int) -> bool:
    count = 0
    while n != 1 and count <= 990: # 990 recursion limit
        count += 1
        n = is_happy_helper(n)
    if count >= 989: # checks if recursion limit is hit
        return False
    return True

    

print(is_happy(19)) # true
print(is_happy(2)) # false 


# longest common prefix
def longest_common_prefix(strs: [str]) -> str:
    if len(strs) == 1:
        return strs[0]
    longest = ""
    strs.sort(key = len)
    for index, char in enumerate(strs[0]):
        # toAdd = True
        for word in strs[1:]:
            if word[index] != char:
                # toAdd = False
                # break
                return longest # we return longest here because it's a prefix. we don't care about the rest. 
                # if we did care about the rest we would add the comments instead
        longest += char
        # if toAdd:
        #     longest += char
    return longest

print(longest_common_prefix(["flow", "flower", "floor"]))



