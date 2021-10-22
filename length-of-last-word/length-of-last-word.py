class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        while s:
            print(s)
            if s[-1] != " ":
                res += 1
                s = s[:-1]
            elif s[-1] == " " and res == 0:
                s = s[:-1]
            else:
                return res
        return res
        