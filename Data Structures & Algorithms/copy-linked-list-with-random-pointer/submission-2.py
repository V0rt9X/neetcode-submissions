"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            copied[current] = copy
            current = current.next
        
        current = head
        while current:
            copied[current].next = copied[current.next]
            copied[current].random = copied[current.random]
            current = current.next
        
        return copied[head]