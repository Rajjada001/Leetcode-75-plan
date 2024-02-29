class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = curr_sum = 0
        min_sum = float('inf')
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_sum = min(min_sum, end-start+1)
                curr_sum -= nums[start]
                start += 1
        return 0 if min_sum==float('inf') else min_sum