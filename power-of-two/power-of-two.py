class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 2251799813685248 % n == 0 
        