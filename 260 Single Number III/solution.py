class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return nums
        helper = 0
        for i in range(len(nums)):
            helper ^= nums[i]
        helper = helper - (helper & (helper - 1))
        helperlist1, helperlist2 = [], []
        for number in nums:
            if helper & number > 0:
                helperlist1.append(number)
            else:
                helperlist2.append(number)
        result1, result2 = 0, 0
        for number in helperlist1:
            result1 ^= number
        for number in helperlist2:
            result2 ^= number
        return [result1, result2]
        