# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        length = 0
        cur=head
        while cur:
            length +=1
            cur = cur.next
        
        rotations = k % length
        if rotations > 0:
            l = r = head
            for i in range(rotations):
                r = r.next
            
            while r.next:
                l = l.next
                r = r.next
            
            nxt = l.next
            l.next = None
            r.next = head
            head = nxt
            
        return head
