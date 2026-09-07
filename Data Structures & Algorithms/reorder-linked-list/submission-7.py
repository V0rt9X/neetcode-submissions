# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        prev = None
        current = l2

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        l2 = prev
        current = l1

        while l1 or l2:
            nxt1, nxt2 = l1.next if l1 else None, l2.next if l2 else None

            current.next = l1
            l1.next = l2
            current = l2
            l1, l2 = nxt1, nxt2

