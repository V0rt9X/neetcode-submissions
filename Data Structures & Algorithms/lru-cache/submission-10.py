class Node:
    def __init__(self,  key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def pop(self, node):
        prev, nxt = node.prev, node.next
        node.prev = node.next = None
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev, nxt.prev, node.next = node, prev, node, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.pop(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.pop(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

            self.insert(node)

            if self.cap < len(self.cache):
                node = self.left.next
                self.pop(node)
                del self.cache[node.key]
                
        
