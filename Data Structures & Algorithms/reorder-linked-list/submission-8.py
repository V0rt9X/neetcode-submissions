# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        l1, l2 = head, prev
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            nxt1, nxt2 = l1.next, l2.next

            current.next = l1
            l1.next = l2
            current = l2

            l1, l2 = nxt1, nxt2
        
        current.next = l1
