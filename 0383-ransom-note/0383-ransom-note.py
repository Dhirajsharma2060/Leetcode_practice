from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter=Counter(ransomNote)
        magazineCounter=Counter(magazine)
        for char in ransomCounter:
            if ransomCounter[char]>magazineCounter[char]:
                return False
        return True         

            
          
        