class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1
        if len(gas) != len(cost) or len(gas) == 0:
            return -1
        if sum(gas) < sum(cost):
            return -1
        start, rem = -1, 0
        for i in range(len(gas)):
            if start == -1 and gas[i] >= cost[i]:
                start = i
                rem += (gas[i] - cost[i])
            elif rem + gas[i] - cost[i] < 0:
                start = -1
                rem = 0
            else:
                rem += (gas[i] - cost[i]) 
        return start