# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        cur = headA
        while cur:
            cur = cur.next;
            lenA += 1
        
        lenB = 0
        cur = headB
        while cur:
            cur = cur.next;
            lenB += 1
        print(lenA, lenB)
        traverseLists = [headA, headB] if lenA > lenB else [headB, headA]
        
        dif = abs(lenA-lenB)
        cur1 = traverseLists[0]
        while dif:
            cur1 = cur1.next
            dif -= 1
            
        cur2 = traverseLists[1]
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
                break
            
            cur1 = cur1.next
            cur2 = cur2.next
        return 
############# Time Complexity: O(m+n) #############
## 1. Find lengths of both lists ---> O(m+n)
## 2. Traverse both lists until intersection found ---> O(max(m, n))
############# Space Complexity: O(1) #############
## 1.