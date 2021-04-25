class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ans, prev, cur, b = 0, 0, 0, ""
        for c in s:
            if c != b:
                ans += min(prev, cur)
                prev, b = cur, c
                cur = 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans
            