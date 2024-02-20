class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(len(nums))]
        prefix = postfix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]

        return res