class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        if max(count.values())==1:
            return sum(count.values())
        else:
            max_count = 0
            c = 0
            for values in count.values():
                if values> max_count:
                    max_count = values
            
            for values in count.values():
                if values == max_count:
                    c += values
            return c