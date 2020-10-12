# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
def reverseLinkedList(l):
    # pointers
    current_node = l
    prev = None
    next = None
    # while loop to traverse l
    while current_node != None:
        next = current_node.next
        # reversal step
        current_node.next = prev
        prev = current_node
        # updates current node
        current_node = next
    return prev  # the last updated prev pointer container the reversed linked lists


def checkBlanagrams(word1, word2):
    # helps with iteration
    word1 = list(word1)
    word2 = list(word2)
    count = 0
    for indx, char in enumerate(word1):
        if char not in word2:
            # keeps track of how many instances of characters have been substituted
            count += 1
        elif count == 2:
            return False
        elif char in word2:
            # remove characters not in then list
            word2.remove(char)
    print(count)
    if count == 1:
        return True
    else:
        return False

# I decided to convert the inputs into lists of individual characters.
# I have a counter that keeps track of how many instances where a character has been substituted.
# The while loop checks whether these two words ar blanagrams by counting when something isn't in another list.
# Return True if the count is 1 meaning there is only one substitute and all other characters are in both lists.

# Can we use binary search to optimize speed?


def findValueSortedShiftedArray(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]: # first search left search space, too see if minimum  exists in the left search space
            if target >= nums[start] and target < nums[mid]: # if the target satisfies this conditions  narrwo the search
                end = mid - 1
            else: # otherwise look at the right search space
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1 # target was not found in the likely search space


# summary:
# I solve this problem by doing a binary search for the target. Basically I am trying to see if the target Is in this rotated sorted array.
# The binary search algorithm creates two search spaces and were trying to narrow the process of finding target by using a midpoint.
# If the target is the midpoint there return True, otherwise continue searching for the target in the while loop.
# if turns out that target is not actually in the potential search space then return -1.


#SpaceComplex
# The time complexity is Olog(N) and the space complexity is O(N).
# This does seem to be the fastest way to find the target, otherwise b/c we don'' \
# ' make loop over the entire array, we only loop through a fraction of it.' \
                                                                                                                                              ' Also were not using any other additional data structure other than the given array.