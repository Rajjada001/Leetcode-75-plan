class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def finder(target):
            start,res,curr_sum =0,0,0
            for end in range(len(nums)):
                curr_sum += nums[end]

                while curr_sum > target and start <= end:
                    curr_sum -= nums[start]
                    start += 1
                res += end-start+1
            return res

        return finder(goal) - finder(goal-1)