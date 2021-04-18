# from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ncols, ans = len(matrix[0]), 0

        # creating the cumulative matrix (in place)
        for row in matrix:
            for col in range(1, ncols):
                row[col] += row[col-1]

        # iterating the cumulative matrix by each window of columns: 0 < [i, j] < len(matrix)
        for start in range(ncols):              # from column j = start
            for end in range(start, ncols):     # to column k = end
                res, csum = {0: 1}, 0   
                for row in matrix:
                    csum += row[end] - (row[start-1] if start else 0) # when j>0
                    if csum - target in res:
                        ans += res[csum-target]
                    res[csum] = res[csum] + 1 if csum in res else 1  
        return ans    