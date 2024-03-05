class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        l,r = 0,len(s)-1
        while l<r and s[l] == s[r]:
            common = s[l]
            while l< r and s[l] == common:
                # prefix = s[:l+1]
                l+=1
            while r>0 and s[r] == common:
                # suffix = s[r-1:]
                r-=1
            # l += 1
            # r-=1
        
        return (r-l+1) if (r-l+1)> 0 else 0
        # 012345678
        # aabccabba
        # ^       ^
        #  ^
        #   ^.   ^
        #   ^.  ^

                