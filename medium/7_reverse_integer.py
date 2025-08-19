# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        range = 2**31 - 1       
        num = 0
        temp = abs(x)             

        while temp != 0:
            rem = temp % 10       
            if num > (range - rem) // 10:
                return 0
            num = num * 10 + rem  
            temp = temp // 10     

        if x < 0:
            return -num            

        return num