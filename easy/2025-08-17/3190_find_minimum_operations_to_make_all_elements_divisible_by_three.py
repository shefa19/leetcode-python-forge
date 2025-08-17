# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.


# Example 1:

# Input: nums = [1,2,3,4]

# Output: 3

# Explanation:

# All array elements can be made divisible by 3 using 3 operations:

# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minimum_number_of_operations = 0
        for num in nums:
            if (num - 1) % 3 == 0:
                minimum_number_of_operations += 1
            elif(num + 1) % 3 ==0:
                minimum_number_of_operations += 1
                
        return minimum_number_of_operations