class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        A = 0
        L = len(nums)
        if L < 2: return A
        if L == 2: return abs(nums[0] - nums[1])
        MIN = min(nums)
        MAX = max(nums)
        
        P = (MAX - MIN) / (L - 1)
        buckets = [[] for _ in range(L-1)]


        
        for num in nums:
            if num == MAX:
                PHN = L-2
            else:
                PHN = int((num - MIN) / P)
            buckets[PHN].append(num)
            
        print(buckets)


        hi_prev = MIN
        index = 0
        for bucket in buckets:
            if len(bucket) == 0: continue
            low_current = min(bucket)
            A = max(A, low_current - hi_prev)
            hi_prev = max(bucket)
        
        return A

            
        