class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            temp = target-num
            if temp in hm:
                return [hm[temp], i]
            else:
                hm[num] = i
            # print(hm)
        