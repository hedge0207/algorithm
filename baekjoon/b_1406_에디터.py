import sys

input = sys.stdin.readline


class Node:
    def __init__(self, char, prev=None, post=None):
        self.char = char
        self.prev = prev
        self.post = post


class LinkedList:
    def __init__(self):
        init_node = Node(None)
        self.head = init_node
        self.tail = None
        self.cur = self.tail

    def insert_node(self, char):
        node = Node(char)
        if self.cur == self.tail:
            if self.tail is not None:
                node.prev = self.tail
                self.tail.post = node
            else:
                node.prev = self.head
                self.head.post = node
            self.tail = node
        else:
            node.post = self.cur.post
            node.prev = self.cur
            self.cur.post.prev = node
            self.cur.post = node
        self.cur = node

    def remove_node(self):
        self.cur.prev.post = self.cur.post
        if self.cur.post is not None:
            self.cur.post.prev = self.cur.prev
        else:
            self.tail = self.cur.prev
        self.cur = self.cur.prev

    def print_list(self):
        cur = self.head.post
        while cur:
            print(cur.char, end="")
            cur = cur.post


text = input().rstrip()
N = int(input())
ll = LinkedList()

for char in text:
    ll.insert_node(char)

for i in range(N):
    command = input().rstrip()
    if command == "L":
        if ll.cur.char is not None:
            ll.cur = ll.cur.prev
    elif command == "D":
        if ll.cur.post is not None:
            ll.cur = ll.cur.post
    elif command == "B":
        if ll.cur.char is not None:
            ll.remove_node()
    else:
        ll.insert_node(command[2])

ll.print_list()