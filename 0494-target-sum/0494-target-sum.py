from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(index, current_sum):
            # Check if the result is already in the memo
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Base case: if we've used all numbers
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Explore adding and subtracting the current number
            add = backtrack(index + 1, current_sum + nums[index])
            subtract = backtrack(index + 1, current_sum - nums[index])
            
            # Store the result in the memo and return it
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]

        # Memoization dictionary to store intermediate results
        memo = {}
        return backtrack(0, 0)
