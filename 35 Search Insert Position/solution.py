class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return None
        l,r = 0,len(nums)-1
        if target>nums[r]:
            return r+1
        while l<r:
            m = (l+r)/2
            if nums[m]==target:
                return m
            if l==m:
                break
            if nums[m]<target:
                 l = m
            else:
                r = m
        return l if target<=nums[l] else l+1
                