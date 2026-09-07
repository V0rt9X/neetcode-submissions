# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                dummy = ListNode()
                current = dummy
                while l1 and l2:
                    nxt1, nxt2 = l1.next, l2.next
                    if l1.val < l2.val:
                        current.next = l1
                        l1 = nxt1
                    else:
                        current.next = l2
                        l2 = nxt2
                    current = current.next
                
                if l1:
                    current.next = l1
                
                if l2:
                    current.next = l2
                
                merged.append(dummy.next)
            
            lists = merged
        
        return lists[0]
