# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        step = 1
        while step <= len(lists):
            for i in range(0, len(lists), step * 2):
                l1 = lists[i]
                l2 = lists[i + step] if (i + step) < len(lists) else None

                lists[i] = self.merge(l1,l2)
            
            step *= 2
        
        return lists[0]
    
    def merge(self, l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        return dummy.next

