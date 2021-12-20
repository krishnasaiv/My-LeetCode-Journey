# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k < 1:
            return head
        ### If the code didn't return in the above statement then 
        ### The Linkedlist has atleast 2 nodes & k >= 2 
        
        totalLength = 0
        cur = head
        while cur:
            totalLength += 1
            cur = cur.next
        
        totalIterTimes = totalLength // k
        
        prev = None
        cur = head
        StartInprevGroup = None
        StartIncurGroup = head
    
        isFirstTime = True
        while cur and totalIterTimes:
            StartIncurGroup = cur
            prev = None
            for i in range(k):
                ### Save pointer to next node
                nxt = cur.next
                
                ### Move connection from cur -> next to cur -> prev
                cur.next = prev
                
                ### Move all the pointers to the right by 1 place
                prev = cur
                cur = nxt
                
            if isFirstTime:
                head = prev
                isFirstTime = False
            else:
                StartInprevGroup.next = prev
            StartInprevGroup = StartIncurGroup
            totalIterTimes -= 1
            
        StartInprevGroup.next = cur
                            
        return head
