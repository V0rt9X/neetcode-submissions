# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2 = list1, list2
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            nxt1,nxt2 = l1.next, l2.next

            if l1.val < l2.val:
                curr.next = l1
                l1 = nxt1
            else:
                curr.next = l2
                l2 = nxt2
            curr = curr.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next
