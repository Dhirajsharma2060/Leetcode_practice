class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        # loop is liye len(s)-1 tak ki jho chratoer each loop me s[i] and s[i+1] agar last gaya to last chracter ke bad bhi number dundega jho milega nahi liye 
        for i in range(len(s)-1):
            total+=abs(ord(s[i])-ord(s[i+1]))
        return total    
        
        