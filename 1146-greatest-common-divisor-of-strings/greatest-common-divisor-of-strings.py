class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # program to find the gcd 
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a
        gcd_num = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_num]

        if str1+str2 == str2+str1:
            return gcd_str
        else:
            return ''


            