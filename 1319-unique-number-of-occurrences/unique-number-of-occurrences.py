class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        res = set()
        for key in hm:
            res.add(hm[key])
        
        if len(hm) == len(res):
            return True
        return False
