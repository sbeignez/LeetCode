class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        dim = len(matrix)
        
        for c in range(dim // 2 + dim % 2):
            for r in range(dim // 2):
                matrix[r][c], matrix[c][dim-1-r], matrix[dim-1-r][dim-1-c], matrix[dim-1-c][r] = \
                matrix[dim-1-c][r], matrix[r][c], matrix[c][dim-1-r], matrix[dim-1-r][dim-1-c]
                
                
        