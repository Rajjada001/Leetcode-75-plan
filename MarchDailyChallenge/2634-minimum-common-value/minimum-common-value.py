class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            if num in s:
                return num
        return -1