# Biweekly Contest 53
# Name: 
# Link: https://leetcode.com/contest/biweekly-contest-53

from typing import List

tests = [
    [[3,5,2,3], 7 ],
    [[3,5,4,2,4,6],8],
    [[3,5], 8 ],

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
import collections

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        A = 0
        nums.sort()
        
        L = len(nums)
        L2 =int(L/2)
        print (nums, L, L2)

        for i in range(L2+1):
            print(i, -1-i, nums[i], nums[-1-i])
            A = max (A, nums[i] + nums[-1-i])

    
        return A

      

            

      
testing(Solution().minPairSum, tests)



