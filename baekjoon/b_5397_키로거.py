import sys

input = sys.stdin.readline


class Node:
    def __init__(self, char, prev=None, post=None):
        self.char = char
        self.prev = prev
        self.post = post


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.cur = self.tail

    def add_node(self, char):
        node = Node(char)
        if self.tail == self.cur:
            if self.tail is None:
                self.tail = node
                self.tail.prev = self.head
                self.head.post = self.tail
            else:
                self.cur.post = node
                node.prev = self.cur
                self.tail = node
        else:
            node.prev = self.cur
            node.post = self.cur.post
            self.cur.post.prev = node
            self.cur.post = node
        self.cur = node

    def remove_node(self):
        if self.cur.post is None:
            self.cur.prev.post = None
            self.tail = self.cur.prev
        else:
            self.cur.prev.post = self.cur.post
            self.cur.post.prev = self.cur.prev
        self.cur = self.cur.prev

    def print_all(self):
        cur = self.head.post
        while cur:
            print(cur.char, end="")
            cur = cur.post
        print()


N = int(input())
texts = [input().rstrip() for _ in range(N)]
for text in texts:
    linked_list = LinkedList()
    for char in text:
        if char == "<":
            if linked_list.cur.char is not None:
                linked_list.cur = linked_list.cur.prev

        elif char == ">":
            if linked_list.cur.post is not None:
                linked_list.cur = linked_list.cur.post

        elif char == "-":
            if linked_list.cur.char is not None:
                linked_list.remove_node()

        else:
            linked_list.add_node(char)
    linked_list.print_all()
