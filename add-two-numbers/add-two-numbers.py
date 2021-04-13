# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def add(l1: ListNode, l2: ListNode, i: int) -> ListNode:
            
            sum = ListNode()
            
            if l1 == None and l2 == None:
                if i == 0:
                    return None
                return ListNode(i)  
            
            if l1 == None:
                l1 = ListNode()
            if l2 == None:
                l2 = ListNode()
            
            sum.val = ((l1.val + l2.val + i) % 10 )    
            sum.next = add(l1.next , l2.next , (l1.val + l2.val + i) // 10)

            return sum
        
        return add(l1,l2,0)
        