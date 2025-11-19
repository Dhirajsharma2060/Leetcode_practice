class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        while original in hashmap:
            original*=2
        return original            

        