# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        length = len(points)
        if length<3:
            return length
        result = -1
        for i in range(length):
            helper = {'inf':0}
            samepoint = 1
            for j in range(i):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    samepoint+=1
                elif points[i].x==points[j].x:
                    helper['inf']+=1
                else:
                    k = 1.0 * (points[j].y-points[i].y)/(points[j].x-points[i].x)
                    if k not in helper:
                        helper[k]=1
                    else:
                        helper[k]+=1
            result = max(result,max(helper.values())+samepoint)
        return result
        