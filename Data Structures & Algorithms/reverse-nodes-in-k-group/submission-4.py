# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevG = dummy

        while True:
            kth = self.findKth(prevG, k)
            if not kth:
                return dummy.next
            
            nextG = kth.next
            current, prev = prevG.next, nextG

            while current != nextG:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
                
            
            tmp = prevG.next
            prevG.next = kth
            prevG = tmp
            

        

    def findKth(self, current, n):
        while current and n > 0:
            current = current.next
            n -= 1
        
        return current