class ListNode:
    def __init__(self, key, val, next_=None):
        self.key = key
        self.val = val
        self.next_ = next_


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 1


class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.map = {}

    def _hash(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_value = self._hash(key)
        if hash_value in self.map:
            linked_list = self.map[hash_value]
            node = linked_list.head
            while node:
                if node.key == key:
                    node.val = value
                    return
                node = node.next_

            linked_list = self.map[hash_value]
            node = ListNode(key, value, linked_list.head)
            linked_list.head = node
            linked_list.size += 1
        else:
            node = ListNode(key, value, None)
            linked_list = LinkedList()
            linked_list.head = node
            self.map[hash_value] = linked_list

    def get(self, key: int) -> int:
        hash_value = self._hash(key)
        if hash_value in self.map:
            node = self.map[hash_value].head
            while node:
                if node.key == key:
                    return node.val
                node = node.next_

        return -1

    def remove(self, key: int) -> None:
        hash_value = self._hash(key)
        if hash_value in self.map:
            ll = self.map[hash_value]
            node = ll.head
            prev = None
            while node:
                if node.key == key:
                    if prev is None:
                        ll.head = node.next_
                    else:
                        prev.next_ = node.next_

                    if ll.size == 1:
                        del self.map[hash_value]
                    return
                prev = node
                node = node.next_

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)