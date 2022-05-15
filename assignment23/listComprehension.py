# list comprehension. again?
# #Assignment - 23 - 01

# ## Write a function that Convert a variable name from camel case to snake case.

# Example :

# camel_case_to_snake_case("learnTechWiseTalentsprint") => learn_tech_wise_talentsprint

# def convert(x):
#     return "_" + x.lower() if x.isupper() else x.lower()

def camel_case_to_snake_case(camel: str) -> str:
    return "".join("_" + x.lower() if x.isupper() else x.lower() for x in camel)

print(camel_case_to_snake_case("learnTechWiseTalentsprint"))


# #Assignment - 23-02

# Write a function that calculate the sum of unique numbers in a given list.

# Example:

# sum_of_unique_numbers([1, 2, 3, 4, 1, 5]) => 14


def sum_of_unique_numbers(num_list: [int])-> int:
    return sum(x for x in num_list if num_list.count(x) == 1)

print(sum_of_unique_numbers([1, 2, 3, 4, 1, 5]))


# #Assignment - 23 - 03

# ##Sum of Two
# Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Examples:

# sum_of_two([2,7,11,15], 9) => [(0,1)] (Explanation: Because nums[0] + nums[1] == 9, we return [0, 1])

# sum_of_two([3,2,4], 6) => [(1,2)]

# sum_of_two([3,3], 6) => [(0,1)]


def sum_of_two(nums: [int], target: int) -> [int]:
    return [(nums.index(first), nums.index(second)) for first in nums for second in nums if first + second == target]

print (sum_of_two([2,7,11,15], 9))