class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) <= 1:
            return 0
        left, right = 0, len(height) - 1
        result = 0
        while left + 1 < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        last = min(height[left], height[right])
        return result if result > last else last
        