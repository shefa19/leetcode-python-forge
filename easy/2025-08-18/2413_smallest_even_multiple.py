# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 

# Example 1:

# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            while b != 0:
                a , b = b, a % b
            return a
        return (2 * n) // gcd(2, n)