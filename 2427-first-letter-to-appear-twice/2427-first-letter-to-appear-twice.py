class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen_letter=[]
        for char in s :
            if char not in seen_letter:
                seen_letter.append(char)
            else:
                return char     