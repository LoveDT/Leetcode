class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        i, j = 2, 2 
        while i<len(nums):
            if nums[i]!=nums[j-2]:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
        