# https://leetcode.com/problems/missing-number/
# Missing numbers
# Given a list nums containing n distinct numbers in the range [0, n], return the smallest number that is not in nums.

def missing_number(nums: [int]) -> int:
    length = len(nums)
    for i in range (0, length+1):
        if i not in nums:
            return i
    return 0

# O(n) time and O(1) space (thought it was O(1) space but it's O(n) space)
def missing_number2(nums: [int]) -> int:
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)



print(missing_number([3,0,1]))
print(missing_number([9,6,4,2,3,5,7,0,1]))
print(missing_number([0]))
print(missing_number([1]))
print(missing_number([0,1]))
print(missing_number([0,1,2]))
print(missing_number([0,1,-2,-1]))
print(missing_number2([0,1,-2,-1]))

# https://leetcode.com/problems/count-largest-group/
# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.


def sum_digits(i: int) -> int:
    return sum([int(x) for x in str(i)])

import statistics

def count_largest_group(n: int) -> int:
    return len(statistics.multimode(sum(map(int, str(i))) for i in range(1, n+1)))


print()
print(count_largest_group(13), 4) # 4
print(count_largest_group(2), 2) # 2
print(count_largest_group(15), 6) # 6
print(count_largest_group(24), 5) # 5
print(count_largest_group(38), 7) # 7
print(count_largest_group(33), 4) # 4
print(count_largest_group(24), 5) # 5
print(count_largest_group(174), 2) # 2