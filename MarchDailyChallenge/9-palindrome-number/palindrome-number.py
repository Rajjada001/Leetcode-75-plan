class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        rev = 0
        while temp:
            d = temp % 10
            rev = rev*10 + d
            temp = temp // 10
        
        print(rev)
        return x == rev