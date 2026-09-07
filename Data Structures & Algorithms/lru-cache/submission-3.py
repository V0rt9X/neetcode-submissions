class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev = node.next = None

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        nxt.prev, node.next = node, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node), self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node), self.insert(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert(node)
        
        if len(self.cache) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        
