class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        #ek finale result le liye or ek total solution se liye 
        res,sol=[],[]
        def backtrack(i):
            if i==n:
                #agar code outofbound ho gaya to
                res.append(sol[:])#[:]this is because we need to add the whole screenshot
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()     
        backtrack(0)
        return res    
        
        