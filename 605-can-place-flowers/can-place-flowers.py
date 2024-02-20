class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        
        count = 0
        f = [0] + nums + [0]

        for i in range(1,len(f)-1):
            if f[i] == 0 and f[i-1]==0 and f[i+1]==0:
                f[i] = 1
                n -= 1
            
        # print(f)
        return n<=0
