class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        if numRows == 1: return s
        for row in range(numRows):
            for i in range( len(s) // (2 * numRows - 2) + 1):
                a = (row + (2 * numRows - 2)* i)
                A = s[a] if a < len(s) else ""
                b = (2 * numRows - 2) * (i+1) - row              
                B = s[b] if (row not in [0, numRows -1]) and (b < len(s)) else ""
                ans = ans + A + B
        return ans  