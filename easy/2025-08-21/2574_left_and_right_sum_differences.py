# You are given a 0-indexed integer array nums of size n.

# Define two arrays leftSum and rightSum where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 

# Example 1:

# Input: nums = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            left_sum = sum(nums[:i])       
            right_sum = sum(nums[i+1:])     
            answer.append(abs(left_sum - right_sum))

        return answer
