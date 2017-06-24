class Solution(object):
    def largestRectangleArea(self, height):
        # write your code here
        if not height or not len(height):
            return 0
        helper = []
        length = len(height)
        result = 0
        for i in range(length+1):
            edge = -1 if i == length else height[i]
            while len(helper) and height[helper[-1]] >= edge:
                hei = height[helper.pop()]
                width = i - helper[-1] - 1 if len(helper) else i
                result = max(result, hei * width)
            helper.append(i)
        return result