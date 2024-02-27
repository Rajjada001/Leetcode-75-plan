class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        count = 0
        max_window = 0
        for end in range(len(nums)):
            if nums[end]==0:
                count += 1
            
            while count > k:
                if nums[start]==0:
                    count -= 1
                start+=1
            max_window = max(max_window, end-start+1)
        return max_window
        
# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2