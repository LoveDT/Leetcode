class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 
        cur, nextnonzero = 0, 0
        while nextnonzero < len(nums):
            while nums[nextnonzero] == 0:
                nextnonzero += 1
                if nextnonzero >= len(nums):
                    return
            if nums[cur] == 0:
                nums[cur], nums[nextnonzero] = nums[nextnonzero], nums[cur]
            cur += 1
            nextnonzero = cur
        return
        