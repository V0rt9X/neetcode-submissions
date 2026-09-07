# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kthEl(head, k):
            curr = head

            while curr and k > 0:
                curr = curr.next
                k -= 1
            
            return curr
        
        dummy = ListNode(0, head)
        prevG = dummy
        
        while True:
            kth = kthEl(prevG, k)
            if kth:
                nextG = kth.next
                kth.next = None
            else:
                break
            
            prev = nextG
            curr = prevG.next
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = prevG.next
            prevG.next = kth
            prevG = tmp
        
        return dummy.next

            
