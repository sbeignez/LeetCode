# Name: Maximum Gap
# Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3761/



from typing import List

tests = [
    [[3,6,9,1], 3 ],
    [[10], 0],
    [[0,1,2,9,10], 7 ],
    [[1,10000000], 9999999],

]
print("TESTS", tests)

def testing(f,tests):
    print("======================")
    success = True
    for i, test in enumerate(tests):
        args = test[:-1]
        expected = test[-1]
        print("-----------------------")
        print(f"Test {i}: {args} --> {expected}.")
        res = f(*args)
        success = success and res==expected
        print(f"{res==expected}\t OUT:{res}\t EXP:{expected}\t IN:{args}\t ")
    print("======================")
    print(f"Success: {success}")

# =============================
import itertools

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
        print(MIN, MAX, MAX-MIN,"L-1",L-1, "P", P)

        for x in range(L-1):
            print(f"[{MIN+x*P}:{MIN+((x+1)*P)}]")

        
        for num in nums:
            if num == MAX:
                PHN = L-2
            else:
                PHN = int((num - MIN) / P)
            print(PHN)
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

      

            

      
testing(Solution().maximumGap, tests)



