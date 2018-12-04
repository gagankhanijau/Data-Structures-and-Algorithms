
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

class Node(object):
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max=capacity
        self.map=dict()
        self.front, self.rear= None, None
        
    def delete_node(self,node):
        if self.front is None: 
            return None
        if self.rear==self.front:
            self.rear=self.front=None
            return node
        if self.front == node:
            self.front= self.front.next
        elif self.rear== node:
            self.rear= self.rear.prev
        node.prev.next= node.next
        node.next.prev= node.prev
        return node
    
    def append_node(self,node):
        if not self.front :
            self.front= self.rear= node
            self.front.prev=self.front.next= node
            return
        node.prev= self.rear
        node.next= self.rear.next
        self.rear.next= node
        self.rear=node
        self.front.prev= self.rear
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key,None)
        if node:
            self.delete_node(node)
            self.append_node(node)
            return node.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node=self.map.get(key,None)
        if node:
            node.val=value
            self.get(key)
            return
        if len(self.map.keys())== self.max:
            node= self.delete_node(self.front)
            self.map.pop(node.key,None)
            del node
        self.map[key] = Node(key,value)
        self.append_node(self.map[key])
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)