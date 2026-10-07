class Node:
    def __init__(self, key=0, value=0):
        # Store the key so we can remove it from the dictionary during eviction.
        self.key = key
        # Store the value associated with the key.
        self.value = value
        # Point to the previous node in the doubly linked list.
        self.prev = None
        # Point to the next node in the doubly linked list.
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Save the maximum number of real entries the cache may contain.
        self.capacity = capacity
        # Map each key to its node for O(1) average lookup.
        self.nodes = {}

        # Dummy nodes make insertion and deletion simpler at both ends.
        self.head = Node()
        self.tail = Node()

        # Initially, the two dummy nodes are connected to each other.
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        # Save the neighboring nodes before changing the links.
        previous_node = node.prev
        next_node = node.next

        # Skip over the node being removed.
        previous_node.next = next_node
        next_node.prev = previous_node

    def _add_to_end(self, node: Node) -> None:
        # The most recently used position is directly before the tail.
        last_real_node = self.tail.prev

        # Connect the new node to the old last node and the dummy tail.
        last_real_node.next = node
        node.prev = last_real_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        # Look up the node in the hash map.
        node = self.nodes.get(key)

        # A missing key is a cache miss and does not change the order.
        if node is None:
            return -1

        # A successful read makes this node the most recently used one.
        self._remove(node)
        self._add_to_end(node)

        # Return the value stored in the cache.
        return node.value

    def put(self, key: int, value: int) -> None:
        # Check whether this key is already in the cache.
        node = self.nodes.get(key)

        if node is not None:
            # Update the existing value because keys must remain unique.
            node.value = value
            # Updating an entry also counts as using it.
            self._remove(node)
            self._add_to_end(node)
            return

        # Create and register a node for a new key.
        new_node = Node(key, value)
        self.nodes[key] = new_node
        self._add_to_end(new_node)

        # If we exceeded capacity, remove the least recently used node.
        if len(self.nodes) > self.capacity:
            least_recent_node = self.head.next
            self._remove(least_recent_node)
            # Delete the evicted key from the hash map as well.
            del self.nodes[least_recent_node.key]
