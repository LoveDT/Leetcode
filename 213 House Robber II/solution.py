class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.maxprofit(nums[:-1]), self.maxprofit(nums[1:]))
        
    def maxprofit(self, nums):
        if not nums or len(nums) == 0:
            return 0
        odd, even = 0, 0
        for i in range(len(nums)):
            if i % 2:
                odd = max(even, odd + nums[i])
            else:
                even = max(odd, even + nums[i])
        return max(odd, even)
                
        