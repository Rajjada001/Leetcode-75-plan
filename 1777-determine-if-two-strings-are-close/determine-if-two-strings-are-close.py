class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        c1 = Counter(count1.values())
        c2 = Counter(count2.values())

        return c1==c2