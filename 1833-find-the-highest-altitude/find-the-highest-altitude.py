class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        max_alt = 0
        for num in gain:
            prefix += num
            max_alt = max(prefix, max_alt)
        return max_alt