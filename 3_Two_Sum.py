"""
Two Sum (Easy)

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up 
to target.

You may assume that each input would have exactly 
one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is 
less than O(n^2) time complexity?
"""

# ------------------------------------
# dataset
nums = [2,7,11,15]
target = 9

nums_2 = [3,2,4]
target_2 = 6

nums_3 = [3,3]
target_3 = 6

nums_4 = [7, 2, 6, 4, 9, 3]
target_4 = 3

# ------------------------------------
# my solution
# time: O(n^2) | space: ?
def mySolution(nums, target):

    indices = []
    for index in range(len(nums)):

        for n_index in range(index + 1, len(nums)):

            if nums[index] + nums[n_index] == target:
                indices.append(index)
                indices.append(n_index)
                return indices

    return indices

print(mySolution(nums_2, target_2))

# ------------------------------------
# optimal solution
# time: O(n) | space: O(n)
def solution(nums, target):

    # val : index
    previousHashMap = {}

    for index, number in enumerate(nums):

        difference = target - number

        # difference value is a key in previousHashMap
        if difference in previousHashMap:

            # previousHashMap[key] returns index value
            return [previousHashMap[difference], index]

        previousHashMap[number] = index

    return

print(solution(nums_2, target_2))