from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left,right=0,n-1
        while left<right:
            curr_summ=numbers[left]+numbers[right]
            if curr_summ==target:
                return (left+1,right+1)
            elif curr_summ<target:
                left+=1
            else:
                right-=1                       