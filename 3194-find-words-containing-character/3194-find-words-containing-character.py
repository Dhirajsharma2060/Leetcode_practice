class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        #ek to humne res bol ke list banaya 
        for i in range(len(words)):
            # if x in the words[i] on that index list then we will append them in the res list  
            if x  in words[i]:
                res.append(i)
            else:
                i+=1    
        return res   

        