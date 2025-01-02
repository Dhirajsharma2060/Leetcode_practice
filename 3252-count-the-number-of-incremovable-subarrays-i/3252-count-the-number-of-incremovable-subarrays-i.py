from typing import List
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                ok = True
                lst = -float('inf')  # Handles all integers

                for k in range(n):
                    if i <= k <= j:
                        continue
                    if lst >= nums[k]:
                        ok = False
                        break
                    lst = nums[k]

                ans += int(ok)
        return ans