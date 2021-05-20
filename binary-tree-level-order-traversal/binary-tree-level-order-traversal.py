# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # null case
        if not root: return []
        
        # Answer and Level
        A = []
        D = deque([root])
        
        while len(D):
            L = []
            for x in range(len(D)):
                node = D.popleft()
                L.append(node.val)
                D.extend( [ n for n in [node.left, node.right] if n])
            A.append(L)
        return A  
            
                
        