class Solution:
    def countPrimes(self, n: int) -> int:
        N = [0] * n
        count = 0
        for x in range(2, n):
            if N[x]: continue
            count += 1
            N[x*x:n:x] = [1] * ((n - 1) // x - x + 1)
        return count  