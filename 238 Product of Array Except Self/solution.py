class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if len(nums)==0 or len(nums)==1:
            return []
        helper1,helper2 = [1],[1]
        for item in nums[:-1]:
            helper1.append(item*helper1[-1])
        for item in nums[1:][::-1]:
            helper2.append(item*helper2[-1])
        return [helper1[i]*helper2[-1-i] for i in xrange(len(helper1))]
        
        