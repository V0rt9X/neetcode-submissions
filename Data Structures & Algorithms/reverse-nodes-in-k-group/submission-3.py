# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup, current = dummy, dummy

        while current:
            kth = self.findKth(current, k)
            if kth == None: return dummy.next

            nextGroup = kth.next

            current, prev = prevGroup.next, nextGroup

            while current != nextGroup:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
            current = prevGroup
        
        return dummy.next


    def findKth(self, current, k):
        if not current: return None

        while current and k > 0:
            current = current.next
            k -= 1
        
        return current
    