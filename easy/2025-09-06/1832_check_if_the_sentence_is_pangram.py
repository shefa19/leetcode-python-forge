# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: falsea

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = True

        letters = set(c for c in sentence if c.isalpha())
        if len(letters) < 26:
            pangram = False
        
        return pangram