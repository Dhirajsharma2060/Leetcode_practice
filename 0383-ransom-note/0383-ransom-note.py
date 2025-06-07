from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter=Counter(ransomNote)
        magazineCounter=Counter(magazine)
        for char in ransomCounter:
            # iska malab ko jab ransomNote ke count value jiyada hoga magazine se then retuen
            #FALSE 
            #example  ransomNote = "aa", magazine = "ab"
            #iska ransome count is {a:2} and magazine ka {a:1 , b:1}
            #because we are checking for individual character so just a then ransomnote ka value 
            # more then magazine ka count so False
            if ransomCounter[char]>magazineCounter[char]:
                return False
        return True         

            
          
        