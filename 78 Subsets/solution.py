class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if len(nums)==0:
            return [[]]
        nums = sorted(nums)
        result = [[]]
        for element in nums:
            result = result + [l + [element] for l in result]
        return result