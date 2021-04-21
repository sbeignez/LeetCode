class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        if len(t) <= 1:
            return t[0][0]
        inf = math.inf
        for row in range(1, len(t)):
            for col in range(row+1):
                t[row][col] += min(
                    t[row-1][col] if col < row else inf,
                    t[row-1][col-1] if col > 0 else inf,
                )
        return min(t[-1])