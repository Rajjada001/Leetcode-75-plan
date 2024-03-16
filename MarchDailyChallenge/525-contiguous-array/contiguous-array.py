class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {}
        seen[0] = -1
        ans = count = 0
        for i, num in enumerate(nums):
            count += 1 if num else -1

            if count in seen:
                ans = max(ans, i-seen[count])
            else:
                seen[count] = i
        return ans