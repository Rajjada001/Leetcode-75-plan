class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        res = set()
        for key,val in hm.items():
            if val in res:
                return False
            else:
                res.add(val)
        return True
