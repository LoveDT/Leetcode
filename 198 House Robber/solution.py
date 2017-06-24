class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        odd,even = 0,0
        for i in range(len(nums)):
            if i%2==0:
                even = max(odd,even+nums[i])
            else:
                odd = max(even,odd+nums[i])
        return max(even,odd)