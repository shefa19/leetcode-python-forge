# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiou"
        index = []

        for i, word in enumerate(s):
            if word.lower() in vowel:
                index.append(i)

        s_list = list(s)

        left, right = 0, len(index) - 1
        while left < right:
            temp = s_list[index[left]]
            s_list[index[left]] = s_list[index[right]]
            s_list[index[right]] = temp

            left += 1
            right -= 1

        return ''.join(s_list)