class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n ** 2) // 4
        else:
            return (n ** 2 - 1) // 4