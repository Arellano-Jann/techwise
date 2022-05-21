def gen_fib(i):
    a, b = 0, 1
    yield a
    for x in range(i):
        yield b
        a, b = b, a+b
        
print(list(gen_fib(5)))

def ith_fib(i: int) -> int:
    if i <= 0:
        return -1
    fib = list(gen_fib(i))
    return fib[-2]

print(ith_fib(5))