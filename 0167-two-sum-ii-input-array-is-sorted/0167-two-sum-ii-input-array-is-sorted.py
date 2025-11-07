class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff not in  hashmap:
                hashmap[numbers[i]]=i
            else:
                return [hashmap[diff]+1,i+1]    


        