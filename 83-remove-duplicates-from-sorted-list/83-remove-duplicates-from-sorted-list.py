# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        start = head
        
        while  start and start.next:
            

            nxt = start.next
            while start.val == nxt.val:
                nxt = nxt.next
                if nxt is None:
                    break
            start.next = nxt
            start = nxt
            
            

        
        return head
        