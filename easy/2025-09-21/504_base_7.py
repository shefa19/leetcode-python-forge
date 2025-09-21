# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 

# Constraints:

# -107 <= num <= 107


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        temp = abs(num)
        result = ""
        while temp > 0:
            result = str(temp % 7) + result
            temp //= 7

        if num < 0:
            result = "-" + result

        return result