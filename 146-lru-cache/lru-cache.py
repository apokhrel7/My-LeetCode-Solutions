# Create doubly linked list data structure
# This data structure will hold key, value pair

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None  # leftmost dummy node holding Least Recently used (LRU) cache
        self.next = None  # rightmost dummy node holding Most Recently Used (MRU) cache


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # maps key to node
        self.capacity = capacity

        # left = LRU, right = most recently used 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        # must be inserted on the right as its recently used

        # prev, nxt = self.right.prev, self.right
        # prev.next = nxt.prev = node
        # node.next, node.prev = nxt, prev

        prev = self.right.prev  # node on left of rightmost dummy node
        prev.next, node.prev = node, prev  # attach node on left to newly inserted node, attach pointer from new node to that prev node
        self.right.prev, node.next = node, self.right   # attach new node to rightmost dummy node


    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the key from its original position and insert it into beginning of cache as it was just accessed
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:

        # if key already in cache
        # since we are inserting same key again, this key is most recently accessed so it needs to be removed and later inserted to most recently accessed position
        if key in self.cache:
            self.remove(self.cache[key])

        # insert the key, node pair into cache
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # remove the node from linked list and cache if capacity has been reached
        if len(self.cache) > self.capacity:
            lru = self.left.next    # LRU will be found on left side of list (right side of dummy node)
            self.remove(lru)        # Remove the node from the list
            del self.cache[lru.key] # Remove the key, pointer pair from cache
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)