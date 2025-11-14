class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        l=0
        res=nums[0]
        for r in range(1,len(nums)):
            if nums[r]<0:
                max_product, min_product = min_product, max_product

            max_product=max(nums[r],max_product * nums[r])
            min_product=min(nums[r],min_product * nums[r])
            print(max_product)
            print(min_product)
            res=max(res,max_product)
        return res             


            





        