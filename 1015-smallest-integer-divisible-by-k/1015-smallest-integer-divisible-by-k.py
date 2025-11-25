class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remain = 0
        l = 0
        for i in range(1, k + 1):
            remain = (remain * 10 + 1) % k
            l += 1
            if remain == 0:
                return l
        return l   
        