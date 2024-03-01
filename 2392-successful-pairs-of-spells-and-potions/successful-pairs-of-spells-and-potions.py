class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n,m = len(spells), len(potions)
        res = []
        potions.sort()
        for spell in spells:
            l,r = 0,m-1
            while l<=r:
                mid = l+(r-l)//2
                product = potions[mid] * spell
                if product >= success:
                    r = mid-1
                else:
                    l = mid+1
            print(l,r)
            res.append(m-l)
        return res