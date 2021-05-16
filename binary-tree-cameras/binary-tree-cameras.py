# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    count = 0
    
    CAMERA = "C"
    MONITORED = "M"
    UNMONITORED = "U"

    states = { 
        (CAMERA, CAMERA) : MONITORED,
        (MONITORED, MONITORED) : UNMONITORED,
        (UNMONITORED, UNMONITORED) : CAMERA,

        (CAMERA, MONITORED) : MONITORED,
        (MONITORED, CAMERA) : MONITORED,
        
        (CAMERA, UNMONITORED) : CAMERA,
        (UNMONITORED, CAMERA) : CAMERA,
        
        (UNMONITORED, MONITORED) : CAMERA,
        (MONITORED, UNMONITORED) : CAMERA,

        (CAMERA, None) : MONITORED,
        (None, CAMERA) : MONITORED,
        (MONITORED, None) : UNMONITORED,
        (None, MONITORED) : UNMONITORED,
        (UNMONITORED, None) : CAMERA,
        (None, UNMONITORED) : CAMERA,
        (None, None) : UNMONITORED,
        }
    
    def minCameraCover(self, root: TreeNode) -> int:

        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1

        def cameraCover(node: TreeNode):

            if not node: return None
            
            state = self.states[(cameraCover(node.right), cameraCover(node.left))]
            if state == self.CAMERA:
                self.count +=1
            return state

        if cameraCover(root) == self.UNMONITORED:
            self.count += 1
            
        return self.count

        
        