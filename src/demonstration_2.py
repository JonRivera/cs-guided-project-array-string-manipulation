"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array.
 Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""


# Understand
# We are incrementing the number that is splitted into individual characters
# convert into string
def plus_one(digits):
    # Your code here
    num = int("".join(str(d) for d in digits)) + 1
    return list(int(n) for n in str(num))


digits = [1, 3, 2]

print(plus_one(digits))


# instructors solutions
def pivot_index(nums):
    # Your code here
    # single-element arrays would just return index 0
    # if there's no left side, consider the left side to be 0
    # if there's no right side, consider the right side to be 0

    # O(n^2) runtime, O(n) space
    # # iterate over the nums
    # for i in range(len(nums)): # O(n)
    #     # figure out the sum of the left side
    #     # use slicing syntax to get everything up to but not including i
    #     # O(n)
    #     left = sum(nums[:i]) # O(i)
    #     # figure out the sum of the right side
    #     # use slicing syntax to get everything after i
    #     right = sum(nums[i+1:]) # O(n - i)
    #     # check if they're equal
    #     if left == right:
    #         # if they're equal, return that index
    #         return i

    # # if we get through the entire loop, we didn't find an element
    # # that satisfied the criteria, so we'll return -1
    # return -1

    # get the sum of all elements in the list
    total = sum(nums)
    # keep track of left sum, which starts off at 0
    left = 0

    # iterate over the length of our nums
    for i, num in enumerate(nums):
        # our right sum is the total - left sum - our current num
        right = total - left - num

        if left == right:
            return i

        # add the previous element to our left sum
        left += num

    return -1


# nums = [1,7,3,6,5,6]
nums = [10, 0]
print(pivot_index(nums))


# Instructors Solution
def plus_one(digits):
    # Your code here
    # turning the list of digits into a string
    # turning the string into an int
    # add one to the int
    # transform the new number back into an array of digits

    # traverse through a digits in reverse
    for i in range(len(digits) - 1, -1, -1):
        # if our right-most digit is a 9
        if digits[i] == 9:
            # change that to a 0
            digits[i] = 0
            # we need to carray a 1 over to the next digit
        # our digit is not a 9
        else:
            # add 1 to our digit
            digits[i] += 1
            # return
            return digits

    # if we get to the end our loop, we had to carry all the way
    # through every digit
    # we need to insert a 1 at the beginning of the digits list
    return [1] + digits


print(plus_one([9, 9, 9]))
