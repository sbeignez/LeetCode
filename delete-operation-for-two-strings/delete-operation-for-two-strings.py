class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cols, rows = len(word1), len(word2)
        dp = [[0] * (cols+1) for _ in range(rows+1)]

        maximun = 0

        for row in range(1,rows+1):
            for col in range(1,cols+1):
                if word1[col-1] == word2[row-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])

        return cols + rows - 2 * dp[-1][-1]    