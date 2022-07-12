"""
Contains Duplicate (Easy)

Given an integer array nums, return true if any value 
appears at least twice in the array, and return false 
if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
* 1 <= nums.length <= 105
* -10^9 <= nums[i] <= 109
"""

# ------------------------------------
# dataset
nums_1 = [1,2,3,1]
nums_2 = [1,2,3,4]
nums_3 = [1,1,1,3,3,4,3,2,4,2]
nums_4 = [1, 2, 3, 4, 5, 6, 7, 3]

# ------------------------------------
# my solution
# time: O(n^2) | space: O(1)
def mySolution(nums):

    # compares every element
    for index in range(len(nums)):

        # loops from index + 1 to compare next element
        for n_index in range(index + 1, len(nums)):

            if nums[index] == nums[n_index]:
                return True
    return False

print(mySolution(nums_3))

# ------------------------------------
# optimal solution
# time: O(n) | space: O(n)
def solution(nums):

    hashset = set()

    for num in nums:

        print("hashset:", hashset)

        if num in hashset:
            return True

        hashset.add(num)

    return False

# print(solution(nums_3))