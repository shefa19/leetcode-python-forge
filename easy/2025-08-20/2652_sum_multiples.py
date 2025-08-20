# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.


# Example 1:

# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum_of_numbers = 0

        for num in range(1, n+1):
            if num % 3 == 0 or num % 5 == 0  or num % 7 == 0:
                sum_of_numbers += num

        return sum_of_numbers