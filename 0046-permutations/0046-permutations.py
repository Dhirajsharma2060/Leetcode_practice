class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans,sol=[],[]
        def backtrack():
            #yaha pe first hamne check kiya ki agar 
            if len(sol)==n:
                #iska matlab ki hamra jho nums me value hai vho pura ho gaya hai 
                ans.append(sol[:])
                return 
            #matlab ki jab array me se number liya hai vho agar sol me hai to mat lena    
            for x in nums:
                if x  not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()

        return ans                 
#TIME COMPLEXITY IS n!

# Space complexity is n 



        