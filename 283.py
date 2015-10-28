# Two cursors pointing the zero and non-zero position for switching the two values. Use temp to jump directly to the last non-zero place.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        temp = 0
        while i < len(nums):
            if nums[i] == 0:
                j = max(i + 1, temp + 1)
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                    temp = j
            i += 1