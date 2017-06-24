class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)