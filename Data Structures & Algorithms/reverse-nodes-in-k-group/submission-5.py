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
                break
            
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
        
        return dummy.next
            

        

    def findKth(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        
        return current