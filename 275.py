# happy number

def num2list(num):
    return [x for x in str(num)]
    
def is_happy_helper(n):
    lst = num2list(n)
    num = 0
    for val in lst:
        num += (int(val) ** 2)
    return num
    

def is_happy(n: int) -> bool:
    count = 0
    while n != 1 and count <= 990:
        count += 1
        n = is_happy_helper(n)
    if count >= 989:
        return False
    return True

    

print(is_happy(19)) # true
print(is_happy(2)) # false 