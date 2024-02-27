class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        # if set(word1) != set(word2):
        #     return False
        count1 = [0]*26
        count2 = [0]*26
        for char in word1:
            count1[ord(char) - ord('a')] += 1
            
        for char in word2:
            count2[ord(char) - ord('a')] += 1

        print(count1, count2) 
        for i in range(26):
            if (count1[i]==0 and count2[i] != 0) or (count1[i]!=0 and count2[i] == 0):
                return False
        
        count1.sort()
        count2.sort()
        return count1 == count2