class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        helper = {}
        for i in range(len(nums)):
            if target - nums[i] in helper:
                return [min(helper[target - nums[i]], i + 1), max(helper[target - nums[i]], i + 1)]
            if nums[i] not in helper:
                helper[nums[i]] = i + 1
        return []