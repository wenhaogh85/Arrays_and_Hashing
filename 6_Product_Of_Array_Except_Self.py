"""
Product of Array Except Self (Medium)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# ------------------------------------
# dataset
nums = [1,2,3,4]
nums_2 = [-1,1,0,-3,3]
nums_3 = [3,4]

# ------------------------------------
# my solution
# time: O(n) | space: ?
def mySolution(nums):

    # if number of elements is less than 2
    # return original result since can't multiple them
    if len(nums) < 3:
        return nums

    else:
        results = []
        for index in range(len(nums)):

            values = []

            # gets all element from the right side except current element
            if index == 0:
                values += nums[index + 1:]

            # gets all element from the left side except current element
            elif index == len(nums) - 1:
                values += nums[:index]

            # gets all element from the left and right side except current element
            else:
                left_sub_array = nums[:index]
                right_sub_array = nums[index + 1:]

                values += left_sub_array + right_sub_array

            # multiply all values stored earlier
            total = 1
            for value in values:
                total = total * value

            results.append(total)

        return results

print(mySolution(nums))

# ------------------------------------
# optimal solution
# time: O(n) | space: ?
def solution(nums):

    result = [1] * len(nums)

    prefix = 1
    for index in range(len(nums)):

        result[index] = prefix

        prefix = prefix * nums[index]

    postfix = 1
    for index in range(len(nums) - 1, -1, -1):

        result[index] = result[index] * postfix

        postfix = postfix * nums[index]

    return result

print(solution(nums))