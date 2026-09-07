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

        l1,l2 = head, slow.next
        slow.next = None

        curr = l2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l2 = prev

        while l1 and l2:
            nxt1,nxt2 = l1.next, l2.next

            l1.next, l2.next = l2, nxt1
            l1,l2 = nxt1, nxt2
        

