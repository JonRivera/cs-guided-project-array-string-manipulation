"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""


# I understand that we want to find the pivot that is
# The index corresponding to the sum of #rs on the left equaled to the sum of numbers to the right
# Plan
# Make a foor loop and check if the starting number up to the current index is equaled to the index to sum of the remaining numbers
# ex) for some nums = [1,2,3] check that sum(nums[0:index]) == sum(nums[index+1:])
#
def pivot_index(nums):
    pivot = -1
    for index in range(1, len(nums)):
        if index + 1 < len(nums) and sum(nums[0:index]) == sum(nums[index + 1:]):
            pivot = index
    return pivot

