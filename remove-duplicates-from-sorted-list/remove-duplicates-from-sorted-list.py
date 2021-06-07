# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        node = head
        while node.next: # loop
            
            tail = node.next
            while tail.val == node.val and tail.next:
                tail = tail.next
            if not tail.next and tail.val == node.val:
                node.next = None
                break
            else:
                node.next = tail
            
            node = node.next # loop

            
        return head
        