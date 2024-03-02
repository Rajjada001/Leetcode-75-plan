class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute Force
        Max = float('-inf')
        maxIdx = -1
        for i,num in enumerate(nums):
            if num > Max:
                Max = num
                maxIdx = i
        return maxIdx
            