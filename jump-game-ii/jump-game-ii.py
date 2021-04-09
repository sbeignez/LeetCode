class Solution:
    def jump(self, nums: List[int]) -> int:        
        L = len(nums)
        x = [L-1 for _ in range(L)]
        x[0] = 0

        for i , v in enumerate(nums):
            for j in range(i+1, min(i+v+1,L)):
                x[j] = min(x[j] , x[i]+1)

        return x[-1]
        