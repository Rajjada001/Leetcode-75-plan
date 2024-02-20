class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        res = ''
        rv = []
        for ch in s:
            if ch in vowels:
                rv.append(ch)
        i = 0
        # reverse the array
        rv = rv[::-1]
        for ch in s:
            if ch in vowels:
                res += rv[i]
                i+=1
            else:
                res += ch
        return res
        