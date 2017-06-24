class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        left, right = 1, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            smaller, greater = 0, 0
            for i in range(len(nums)):
                if nums[i] >= left and nums[i] <= mid:
                    smaller += 1
                if nums[i] > mid and nums[i] <= right:
                    greater += 1
            if smaller > greater:
                right = mid
            else:
                left = mid
        count = 0
        for i in range(len(nums)):
            if nums[i] == left:
                count += 1
            if count > 1:
                return left
        return right
        
        
        