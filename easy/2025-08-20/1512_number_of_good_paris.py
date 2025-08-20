# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        length_of_nums = len(nums)
        good_pairs = 0

        for i in range(length_of_nums):
            for j in range(i + 1, length_of_nums):
                if nums[i] == nums[j]:
                    good_pairs += 1
        return good_pairs
    

nums = [1,2,3,1,1,3]
obj = Solution()
print(obj.numIdenticalPairs(nums))
