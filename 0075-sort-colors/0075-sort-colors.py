class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        i = 0
        for color, freq in sorted(hashmap.items()):
            for _ in range(freq):
                nums[i] = color
                i += 1        

       