# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #### To rotate a linked list by k places, we have to reach k+1th node from the end
        #### Reduce k to kRem so that 1 <= kRem <= length-1 by taking the reminder of length when divided by k
        
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
    
############# Time Complexity: O(n) #############
## 1. Find length ---> O(n)
## 2. Navigate to the n+1 th node from the end ---> O(n)

############# Space Complexity: O(1) #############
## 1. No Extra space --> O(1)