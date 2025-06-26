class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={"}":"{",")":"(","]":"["}
        stack=[]
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop()!=hashmap[char]:
                        return False
        return not stack            

