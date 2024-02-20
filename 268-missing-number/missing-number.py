class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalNum = n*(n+1)//2
        given_num = sum(nums)

        res = totalNum - given_num
        return res