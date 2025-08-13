# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = y = 0
        for n in nums:
            x += n
            if n > 9:
                while n != 0:
                    y += n % 10
                    n //= 10
            else:
                y += n
        
        return abs(x - y)
        

