"""
Group Anagrams (Medium)

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters
exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
* 1 <= strs.length <= 104
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.
"""

# ------------------------------------
# dataset
strs = ["eat","tea","tan","ate","nat","bat"]
strs_2 = [""]
strs_3 = ["a"]

# ------------------------------------
# my solution
# time: ? | space: ?
def mySolution(strs):

    groups = []

    used_index = []
    for index in range(len(strs)):

        group = []

        # prevents duplicate anagram if anagram has been added before
        if index not in used_index:
            group.append(strs[index])

        for n_index in range(index + 1, len(strs)):

            # checks if element and subsequent elements are anagram
            if sorted(strs[index]) == sorted(strs[n_index]):

                # checks if this element's index or n_index has been added
                # to previous sub-group before using used_index list
                if index not in used_index and n_index not in used_index:

                    used_index.append(n_index)

                    anagram = strs[n_index]
                    group.append(anagram)

        used_index.append(index)

        if len(group) > 0:
            groups.append(group)

    return groups

print(mySolution(strs))

# ------------------------------------
# optimal solution
# time: O(m * n) | space: ?

from collections import defaultdict

def solution(strs):

    # mapping character count to list of anagrams
    result = defaultdict(list)

    for string in strs:

        # initialises key (count)
        # number of letter from a - z
        count = [0] * 26

        # construct count key by updating its values
        # in terms of frequency count for each character
        # in the string
        for character in string:
            count[ord(character) - ord("a")] += 1

        # append string value into defaultdic based on
        # constructed count key
        result[tuple(count)].append(string)

    # returns only the values of the result and not the keys
    return result.values()

print(solution(strs))