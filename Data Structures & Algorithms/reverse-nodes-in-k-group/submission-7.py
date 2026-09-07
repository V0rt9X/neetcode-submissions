# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findKth(node):
            i = 0
            while node and i < k:
                node = node.next
                i += 1
            
            return node if i == k else None
        
        dummy = ListNode(0, head)
        prevG = dummy
        current = dummy.next

        while current:
            kth = findKth(prevG)
            if kth == None:
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
        
        return dummy.next