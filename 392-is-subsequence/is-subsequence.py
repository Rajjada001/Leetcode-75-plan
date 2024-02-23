class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_len, s_len = 0, 0
        while s_len<len(s) and t_len<len(t):
            if s[s_len] == t[t_len]:
                s_len+=1
            t_len+=1
        return s_len==len(s)
        