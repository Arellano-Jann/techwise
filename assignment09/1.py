# Write a program that produces a tableau like this

#  13  17 + 

#   6  34 × 

#   3  68 + 

#   1 136 + 

# =221 

# Remember that the algorithm is : Halve and double; Add the  + s, skip the  × s. The purpose is to also do a bit of output formatting
#  the  × s are rows that have left side even

def rus_mult_print(a: int, b: int) -> None:
    #Write your code Here
    if a % 2 == 0:
        print(a, b, "×")
        return rus_mult_print(a // 2, b*2)
    if a == 1:
        print(a, b, "+")
        return b
    print(a, b, "+")
    # print("=", b)
    return b + rus_mult_print(a // 2, b*2)

print(rus_mult_print(13, 17))


def line(num_stars: int) -> str: # returns a line of n *'s
    return "*" + (num_stars * " *") + ""

def make_triangle(n): # returns list of stars
    triangle = []
    for i in range(n):
        triangle.append(line(i))
    return triangle

# How to produce an upside down triangle?

def upside_down_triangle(length: int):
    #write your code here
    triangle = make_triangle(length)
    spaced_triangle = []
    for i in triangle[::-1]:
        spaced_triangle.append(i.center(length*10))
    return "\n".join(spaced_triangle)

print(upside_down_triangle(7))

# How to produce a right_angled triangle?

def right_angle(length: int):
    #write your code here
    triangle = make_triangle(length)
    spaced_triangle = []
    for i in triangle:
        spaced_triangle.append(i.center(0))
    return "\n".join(spaced_triangle)

print(right_angle(7))

# How to produce a right_angled triangle, facing the other way?

def right_angle_opp(length: int):
    #write your code here
    triangle = make_triangle(length)
    spaced_triangle = []
    for i in triangle:
        spaced_triangle.append('%50s' % i)
    return "\n".join(spaced_triangle)

print(right_angle_opp(7))

# How to produce a diamond?

def diamond(length: int):
    #write your code here
    triangle = make_triangle(length)
    spaced_triangle = []
    for i in triangle:
        spaced_triangle.append(i.center(length*10))
    for i in triangle[length-2::-1]:
        spaced_triangle.append(i.center(length*10))
    return "\n".join(spaced_triangle)

print(diamond(13))