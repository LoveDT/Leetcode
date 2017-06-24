class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        n = len(num)
        result_map = {}
        for number in num:
	        if number not in result_map:
		        result_map[number]=0
	        result_map[number]+=1
        result = [item[0] for item in result_map.items()]
        result_ind = [item[1] for item in result_map.items()]
        ind = result_ind.index(max(result_ind))
        return result[ind]