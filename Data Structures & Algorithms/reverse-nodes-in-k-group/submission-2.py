# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.findKth(prevGroup, k)
            if not kth: 
                return dummy.next
            
            nextGroup = kth.next
            current = prevGroup.next
            prev = nextGroup

            while current != nextGroup:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp



    def findKth(self, start, k):
        current = start

        while current and k > 0:
            current = current.next
            k -= 1
        
        return current
    


