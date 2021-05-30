# Biweekly Contest 53
# Name: 5756. Minimum XOR Sum of Two Arrays
# Link: https://leetcode.com/contest/biweekly-contest-53/problems/minimum-xor-sum-of-two-arrays/

from typing import List

tests = [
    [[1,2], [2,3], 2],

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
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        A = 0
        N = len(nums1)
        R = []
        for N2 in itertools.permutations(nums2, N):
            S = 0
            for x, y in zip(nums1, N2):
                S += (x ^ y)
            R.append(S)

        # S = sum(map(lambda x, y: x ^ y , zip(nums1, nums2)))
        # print(S)
       
        
        return min(R)

      

            

      
testing(Solution().minimumXORSum, tests)



