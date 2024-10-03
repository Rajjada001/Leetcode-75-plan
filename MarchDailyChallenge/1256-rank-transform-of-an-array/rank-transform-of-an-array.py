class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rm = {}
        rank = 1
        for val in sorted(set(arr)):
            rm[val] = rank
            rank += 1
        
        result = [rm[val] for val in arr]
        return result
