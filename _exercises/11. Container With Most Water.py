# Name: 
# Link: https://leetcode.com/explore/challenge/


from typing import List

tests = [
    [[1,1], 1 ],
    [[1,2,3,4,5], 6],
    [[1,1,2,1,1], 4], 
    [[1,8,6,2,5,4,8,3,7], 49],
    [[2,3,4,5,18,17,6], 17]

]
print("TESTS", tests)

def testing(f,tests):
    print("  ======================")
    success = True
    for i, test in enumerate(tests):
        args = test[:-1]
        expected = test[-1]

        print(f"  Test {i}: {args} --> {expected}.")
        res = f(*args)
        success = success and res==expected
        print(f"  {res==expected}\t OUT:{res}\t EXP:{expected}\t IN:{args}\t ")
        print("  -----------------------")
    print(f"  Success: {success}")
    print("  ======================")


# =============================
import itertools

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 2:
            return min(height)**2

        def area(A, i, j):
            return min(A[i] , A[j]) * (j - i)

        a, z = 0, len(height)-1
        i, j = a, z

        print("(", height[i], ", ", height[j], ") *", (j - i - 1), "=", area(height, i, j))

        while a < z and i < j:

            if height[i] <= height[j]:
                i = i+1
            else:
                j = j-1

            if area(height, i, j) > area(height, a, z) and i != j :
                a, z = i, j

            print("(", height[i], ", ", height[j], ") *", (j - i - 1), "=", area(height, i, j))


        return area(height, a, z)
            
      
testing(Solution().maxArea, tests)



