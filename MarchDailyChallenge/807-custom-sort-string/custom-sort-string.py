class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cs = Counter(s)
        res = ''
        for o in order:
            if o in cs:
                res += o * cs[o]
                cs[o] = 0
        
        for char, count in cs.items():
            res += char * count
        
        return res
            
        print(co, cs)
        return s