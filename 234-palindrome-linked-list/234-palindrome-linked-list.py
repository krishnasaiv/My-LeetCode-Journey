# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next is None:
            return True
        
        #### Find the middle node
        l = r = head
        while r.next and r.next.next:
            l = l.next
            r = r.next.next
        
        #### Break connection to SecondHalf of LinkedList
        SecondHalf = l.next
        l.next = None
        
        
        #### Reverse the linkedlist after l
        prev = None
        cur = SecondHalf
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        #### Reconnect the original tail to the first half of linkedlist
        l.next = prev
        
        #### Move l to start & r to prev( start of reversed secondhalf ) & compare each node while iterating
        l = head
        r = prev
        
        while r:
            # print(l, r)
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
        