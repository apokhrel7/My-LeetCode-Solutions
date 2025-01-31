# Create node class
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}       # map the key to node

        # left = LRU, right = MRU (most recently used)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # attach the LRU and MRU (most recently used) to each other in beginning

    # remove node from list
    def remove(self, node):
        # nextNode = node.next  # node that is going to be at leftmost position now
        node.prev.next, node.next.prev = node.next, node.prev

        # # attach new node next to LRU node
        # self.left.next = nextNode
        # nextNode.prev = self.left





    # insert node at right
    def insert(self, node):
        prevNode = self.right.prev
        self.right.prev, node.next = node, self.right
        node.prev, prevNode.next = prevNode, node 
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # TODO: update most recently used

            # we need to remove the key-value pair from left (LRU) and reinsert it back to the right (MRU)
            # this way we can capture LRU and MRU nodes
            self.remove(self.hashmap[key])  
            self.insert(self.hashmap[key])

            return self.hashmap[key].val   # hashmap[key] = pointer of node, so use .val to determine the actual node value

        return -1

    def put(self, key: int, value: int) -> None:

        # remove node if already exists
        if key in self.hashmap:
            self.remove(self.hashmap[key]) 

        # insert new node to list
        newNode = Node(key, value)
        self.hashmap[key] = newNode
        self.insert(self.hashmap[key])  

        if len(self.hashmap) > self.cap:
            # remove from linkedin list and delete the LRU from hashmap

            lru = self.left.next
            self.remove(lru)        # remove from linked list
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)