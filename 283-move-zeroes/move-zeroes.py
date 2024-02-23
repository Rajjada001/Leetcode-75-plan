class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        j = 0
        for i in range(len(nums)):
            if nums[i]==0:
                k += 1
            else:
                nums[j] = nums[i]
                j+=1
        # print(j,k,nums)

        for i in range(len(nums)-j):
            nums[j] = 0
            j+=1
        return nums

        