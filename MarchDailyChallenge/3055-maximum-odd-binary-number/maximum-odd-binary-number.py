class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countOnes = 0
        countZero = 0
        for ch in s:
            if ch == '1':
                countOnes += 1
            else:
                countZero += 1
        res = ''
        for i in range(countOnes-1):
            res += '1'
        for i in range(countZero):
            res += '0'
        
        return res+'1'
            
        