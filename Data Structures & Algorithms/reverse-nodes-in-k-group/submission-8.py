# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        prevG = dummy
        current = prevG.next

        while True:
            kth = self.find_kth(prevG, k)
            if not kth:
                return dummy.next
            
            nextG = kth.next
            kth.next = None
            prev = nextG
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            tmp = prevG.next
            prevG.next = prev
            prevG = tmp
            current = prevG.next

        
    def find_kth(self, start, k1):
        counter = 0
        found = start

        while found and counter != k1:
            found = found.next
            counter += 1
        
        return found
