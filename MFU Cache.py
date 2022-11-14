from collections import OrderedDict, defaultdict

class Node:
    def __init__(self, value, count):
        self.value = value
        self.count = count

class MFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.node_keys = {}
        # dict of value having ordered_dict as key by default
        self.node_counts = defaultdict(OrderedDict)
        # Lest frequently used bucket, to free up when the capacity is full
        self.min_count = None
    
    def get(self, key):
        if not key in self.node_keys:
            return -1

        node = self.node_keys[key]
        del self.node_counts[node.count]

        node.count +=1 
        self.node_counts[node.count][key] = node

        # See if the min_count is empty
        if not self.node_counts[self.min_count]:
            self.min_count += 1

        return node.val

    def put(self, key):
        if not self.capacity:
            return
        
        if key in self.node_keys:
            self.node_keys[key] = value
            self.get(key)
            return
        
        if len(self.node_keys) == self.capacity:
            lfu_key, lfu_node = self.node_counts[self.min_count].popitem(last=False)
            del self.node_keys[lfu_key]

        new_node = Node(key, 1)
        self.node_keys[key] = new_node
        self.node_counts[1][key] = new_node
        self.min_count = 1
