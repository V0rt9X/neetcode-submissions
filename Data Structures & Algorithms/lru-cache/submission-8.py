class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev, self.next = None, None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node


    
    def pop(self, node):
        prev, nxt = node.prev, node.next

        prev.next, nxt.prev = nxt, prev
        node.next = node.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.pop(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        else:
            node = self.cache[key]
            self.pop(node)
            self.insert(node)
            node.val = value

        if len(self.cache) > self.capacity:
            node = self.left.next

            del self.cache[node.key]
            self.pop(node)

        
