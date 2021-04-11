# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def deep(trees: List) -> int:            
            leaves = [ t.left for t in trees if t.left] + [ t.right for t in trees if t.right]
            if not leaves:
                return sum(leaf.val for leaf in trees)
            return deep(leaves)

        return deep([root])        