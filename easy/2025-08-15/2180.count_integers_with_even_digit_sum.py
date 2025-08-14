# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.


class Solution:
    def countEven(self, num: int) -> int:
        number_of_positive_integer = 0
        for i in range(2, num+1):
            if i < 10 and i % 2 == 0:
                number_of_positive_integer += 1
            else:
                sum_of_digits = 0
                while i != 0:
                    sum_of_digits += i % 10
                    i //= 10
                if sum_of_digits % 2 == 0:
                    number_of_positive_integer += 1
        
        return number_of_positive_integer           