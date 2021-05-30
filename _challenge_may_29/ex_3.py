# Biweekly Contest 53
# Name: 
# Link: https://leetcode.com/contest/biweekly-contest-53

from typing import List

tests = [
    [[[1,2,3],[4,5,6],[7,8,9]], [20,9,8] ],
    [[[7,7,7]],[7]],
    [[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]], [228,216,211]],
    [[[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]], [107,103,102]],

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
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        A = set()
        M = len(grid[0])
        N = len(grid)
        print("grid", M,N)

        for row, rows in enumerate(grid):
            for col, cols in enumerate(rows):
                print("row, col", row, col)
                i = 0
                while row - i >=0 and row + i <  N and col - i >=0 and col + i < M:
                    if i == 0:
                        A.add(grid[row][col])
                    else:
                        S = 0
                        for x in range(i):
                            S += grid[row+i-x][col-x]
                            S += grid[row-i+x][col+x]
                            S += grid[row+x][col+i-x]
                            S += grid[row-x][col-i+x]
                        A.add(S)
                    i += 1  
                print("max i ", i)
        A = list(A)
        print(A)
        A.sort(reverse=True)
        return A[0:3]

      

            

      
testing(Solution().getBiggestThree, tests)



