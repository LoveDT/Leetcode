class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        if len(nums)==0:
            return [[]]
        nums = sorted(nums)
        result, prev, count = [[]], None, -1
        for element in nums:
            if element != prev:
                prev, count = element, len(result)
            result = result + [l + [element] for l in result[len(result)-count:]]
        return result
        