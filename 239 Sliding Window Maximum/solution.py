class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        helper = collections.deque()
        result = []
        for i in range(len(nums)):
            while helper and nums[i]>=nums[helper[-1]]:
                helper.pop()
            helper.append(i)
            if helper[0]==i-k:
                helper.popleft()
            if i>=k-1:
                result.append(nums[helper[0]])
        return result
        