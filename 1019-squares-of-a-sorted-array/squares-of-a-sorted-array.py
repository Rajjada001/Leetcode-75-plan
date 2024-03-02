class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        res = [0]*len(nums)
        k = len(nums)-1
        while l<=r:
            if abs(nums[l]) < abs(nums[r]):
                res[k] = nums[r] * nums[r]
                r-=1
            else:
                res[k] = nums[l] *nums[l]
                l+=1
            k-=1
        return res