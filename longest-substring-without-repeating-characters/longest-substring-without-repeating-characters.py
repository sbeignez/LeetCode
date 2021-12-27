class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sub = ""
        m = 0
        
        for c in s:
            if c not in sub:
                sub = sub + c
                m = max(m, len(sub))
            else:
                sub = sub[ sub.find(c)+1 : ] + c

        return m