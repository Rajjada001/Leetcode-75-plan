class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        l,r = 0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                s1,s2 = isPalindrome(s,l+1,r), isPalindrome(s,l,r-1)
                return s1 or s2
            l+=1
            r-=1
        
        return True