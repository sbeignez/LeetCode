# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        A = []
        if not root: return A
    
        D = deque([root])
        
        while len(D):
            L = []
            for _ in range(len(D)):
                node = D.popleft()
                L.append(node.val)
                if node.left: D.append(node.left)
                if node.right: D.append(node.right)
            A.append(L)
        return A  
            
                
        