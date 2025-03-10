# Time Complexity : 
    # put() -> O(1)
    # get() -> O(1)

# Space Complexity : O(N)

# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # store the key: node-address
        self.head = ListNode(float('inf'), float('inf'))
        self.tail = ListNode(float('inf'), float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
    
    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        prev_node.next.prev = prev_node
        node.prev = None
        node.next = None
    
    def append(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        # search for key in cache
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # update operation
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.append(node)
            return
        
        # add operation
        if (len(self.cache) == self.capacity):
            del self.cache[self.head.next.key]
            self.remove(self.head.next)
            
        new_node = ListNode(key, value)
        self.append(new_node)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)