# Name: 00. Maximum Erasure Value
# Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3758/


'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

'''

# =============================
from typing import List

# =============================
tests = [
    [[4,2,4,5,6], 17],
    [[5,2,1,2,5,2,1,2,5], 8],
    [[10000], 10000],
    [[100,1,2,1,1,2,3] , 100],
]
print("TESTS", tests)

# =============================
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
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        inside = set()
        runsum = 0
        i, j = 0, 0

        while i < len(nums):
            while j < len(nums):
                # print(i, j)
                if i == j:
                    inside.clear()
                    inside.add(nums[i])
                    runsum = nums[i]
                    maxsum = max(maxsum, runsum)
                elif nums[j] not in inside:
                    inside.add(nums[j])
                    runsum += nums[j]
                    maxsum = max(maxsum, runsum)
                else:
                    while nums[j] in inside:
                        inside.remove(nums[i])
                        runsum -= nums[i]
                        i += 1
                    inside.add(nums[j])
                    runsum += nums[j]
                print(nums[i:j+1], runsum, inside)
                j += 1
            i += 1

        return maxsum

class Solution:
    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        n = nums[0]
        maxsum, runsum = n, n
        inside = {n}
        i, j = 0, 1

        # rest = [ sum(nums[i:]) for i in range(len(nums)) ]

        while i < len(nums):
            while j < len(nums):
                while nums[j] in inside:
                    inside.remove(nums[i])
                    runsum -= nums[i]
                    i += 1
                inside.add(nums[j])
                runsum += nums[j]
                maxsum = max(maxsum, runsum)
                # if runsum + rest[j] < maxsum:
                #     return maxsum
                j += 1
            i += 1
        return maxsum

            

      
testing(Solution().maximumUniqueSubarray2, tests)



