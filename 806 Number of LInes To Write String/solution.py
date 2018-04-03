class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S or len(S) == 0:
            return [0, 0]
        if not widths or len(widths) != 26:
            return [0, 0]
        cur_line = 1
        cur_unit = 0
        for letter in S:
            cur_letter_index = ord(letter) - ord("a")
            cur_unit += widths[cur_letter_index]
            if cur_unit > 100:
                cur_line += 1
                cur_unit = widths[cur_letter_index]
        
        return [cur_line, cur_unit]
        