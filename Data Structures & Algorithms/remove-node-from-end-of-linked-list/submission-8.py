# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        dummy = ListNode(0, prev)
        current = dummy
        prev = None

        while current and n != 0:
            prev = current
            current = current.next
            n -= 1
        
        prev.next = current.next

        current = dummy.next
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev
