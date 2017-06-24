class Solution(object):
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return []
        left, right = 0, len(nums) - 1
        while left < len(nums) and nums[left] == 0:
            left += 1
        while right > -1 and nums[right] == 2:
            right -= 1
        count = left
        while count < right + 1:
            if nums[count] == 2:
                nums[right], nums[count] = nums[count], nums[right]
                while nums[right] == 2:
                    right -= 1
            if nums[count] == 0:
                nums[left], nums[count] = nums[count], nums[left]
                left += 1
            count += 1
        return
            
