class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        leng = len(nums)
        if leng==0:
            return 0
        i,j = 0,0
        while i<leng:
            if nums[i]!=val:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j
        