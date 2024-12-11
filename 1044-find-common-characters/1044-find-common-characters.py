class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_count=Counter(words[0]) 
        for word in words:
            word_count &= Counter(word)
        return list(word_count.elements())          
                
        