"""
Valid Anagram (Easy)

Given two strings s and t, return true if t 
is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed 
by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
* 1 <= s.length, t.length <= 5 * 104
* s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""

# ------------------------------------
# dataset
s = "anagram"
t = "nagaram"

a = "rat"
b = "car"

# ------------------------------------
# my solution
def mySolution(s, t):
    return sorted(s) == sorted(t)

# print(mySolution(a, b))

# ------------------------------------
# optimal solution
# time: O(s + t) | space: O(s + t)
def solution(s, t):

    if len(s) != len(t):
        return False

    # frequencies of each char in each string
    countS = {}
    countT = {}

    for index in range(len(s)):

        # key -> value
        # "a" = 1 + value (frequency count) of "a"
        countS[s[index]] = 1 + countS.get(s[index], 0)
        countT[t[index]] = 1 + countT.get(t[index], 0)

    for n_index in countS:
        if countS[n_index] != countT.get(n_index, 0):
            return False

    return True

print(solution(a, b))