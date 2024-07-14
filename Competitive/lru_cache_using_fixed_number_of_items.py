
ITEMS_IN_CACHE = 4


# A doubly linked list will keep the numbered items
class DoubleNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item_count = 2
        self.cache = dict()
        self.left, self.right = DoubleNode(0, 0), DoubleNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def __repr__(self):
        this = self.left
        result = ""
        while this:
            result += f"{this.val}->"
            this = this.next
        return result

    def _remove_node(self, node):

        if node.key in self.cache:
            del(self.cache[node.key])
        prev, nex = node.prev, node.next
        if prev:
            prev.next = nex
        if nex:
            nex.prev = prev
        node.next, node.prev = None, None
        self.item_count -= 1

    def _insert_node(self, node):
        self.cache[node.key] = node
        node.next = self.left
        self.left.prev = node
        self.left = node
        self.item_count += 1

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if node == self.right:
                    self.right = node.prev
            self._remove_node(node)
            self._insert_node(node)
            return node.val
        return -1

    def put(self, key, val):
        if self.item_count == self.capacity:
            right_node = self.right
            self.right = right_node.prev
            self._remove_node(right_node)
        new_node = DoubleNode(key, val)
        self._insert_node(new_node)


if __name__ == "__main__":
    lru_cache = LRUCache(ITEMS_IN_CACHE)
    lru_cache.put(1, "a")
    lru_cache.put(2, "b")
    print(lru_cache.get(1))
    lru_cache.put(3,"c")
    lru_cache.put(4, "d")
    print(lru_cache.get(2))
    lru_cache.put(5, "e")
    a = input()







