class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits=0
        left=0
        res=0
        count={}
        for right in range(len(fruits)):
            if fruits[right] not in count:
                count[fruits[right]]=0
            count[fruits[right]]+=1
            max_fruits+=1

            while len(count)>2:
                f=fruits[left]
                count[fruits[left]]-=1
                max_fruits-=1
                left+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,max_fruits)     
        return res       

