# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        nodes = []
        while head:
            nodes += [head.val]
            head = head.next
        
        def grow(nodes) -> TreeNode:
            if not nodes: return None
            return TreeNode(
                nodes[len(nodes)//2],
                grow(nodes[:len(nodes)//2]),
                grow(nodes[len(nodes)//2+1:]))

        return grow(nodes)
        