class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq = total_freq = 0

        for num in nums:
            freq[num] = freq.get(num, 0)+1
            frequency = freq[num]

            if frequency > max_freq:
                max_freq = frequency
                total_freq = frequency
            elif frequency == max_freq:
                total_freq += frequency
        
        return total_freq