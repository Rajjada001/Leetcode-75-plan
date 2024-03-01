class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = sorted(s)
        one_cnt = s.count('1')
        zero_cnt = s.count('0')

        res = '1'*(one_cnt - 1) + '0'*(zero_cnt) + '1'
        return res