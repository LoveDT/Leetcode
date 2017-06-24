class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums==[]:
            return 0
        if len(nums)==1:
            return 1
        i,j = 1,1
        leng = len(nums)
        while i<leng:
            if nums[i]!=nums[i-1]:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j        