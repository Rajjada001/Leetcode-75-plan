class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        for i in range(len(nums)):
            prevOk = i==0 or nums[i-1]==0
            nextOk = i==len(nums)-1 or nums[i+1]==0
            if prevOk and nums[i]==0 and nextOk:
                nums[i] = 1
                n -= 1
        return n<=0