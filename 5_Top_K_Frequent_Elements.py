"""
Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
* 1 <= nums.length <= 105
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""

# ------------------------------------
# dataset
nums = [1,1,1,2,2,3]
k = 2

nums_2 = [1]
k_2 = 1

# ------------------------------------
# my solution
# time: ? | space: ?
def mySolution(nums, k):
    
    hashset = {}

    # loops every number in nums and update their frequecies
    # using a hashset
    for number in nums:
        hashset[number] = 1 + hashset.get(number, 0)

    # sorts hashset in descending order based on frequency (value)
    sortedHashset = dict(sorted(hashset.items(), key=lambda item: item[1], reverse=True))

    keys = list(sortedHashset.keys())

    return keys[:k]

print(mySolution(nums, k))

# ------------------------------------
# optimal solution (using a variation of bucket sort)
# time: O(n) | space: O(n)
def solution(nums, k):

    hashmap = {}
    frequencies = [[] for index in range(len(nums) + 1)]

    for number in nums:
        hashmap[number] = 1 + hashmap.get(number, 0)

    # key (number), value (frequencies)
    for number, frequency in hashmap.items():
        frequencies[frequency].append(number)

    result = []
    for index in range(len(frequencies) - 1, 0, -1):

        for number in frequencies[index]:

            result.append(number)

            if len(result) == k:
                return result

print(solution(nums, k))