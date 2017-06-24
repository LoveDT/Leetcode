class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        helper = {}
        for number in nums:
            if number not in helper:
                helper[number]=1
            else:
                helper[number]+=1
        result = []
        for element in helper:
            if helper[element]>(len(nums)/3):
                result.append(element)
        return result