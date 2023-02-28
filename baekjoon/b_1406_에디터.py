import sys


input = sys.stdin.readline

class Node:
    def __init__(self, char, pre=None, pos=None):
        self.char = char
        self.pre = pre
        self.pos = pos


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        cur = linked_list.head.pos
        while cur:
            print(cur.char, end="")
            cur = cur.pos
        print()
        cur = linked_list.tail
        while 1:
            print(cur.char, end="")
            cur = cur.pre
            if cur.char=="H":
                break
        print()
        print("-"*100)


    def link_nodes(self, elements):
        for i in range(len(elements)):
            node = Node(text[i])
            if linked_list.tail is None:
                linked_list.head = node
            else:
                node.pre = linked_list.tail
                linked_list.tail.pos = node
            linked_list.tail = node
            self.size += 1

    def add_head(self):
        cur_head = self.head
        new_head = Node("H", None, cur_head)
        self.head = new_head
        cur_head.pre = new_head



text = input().rstrip()
linked_list = LinkedList()
linked_list.link_nodes(text)
linked_list.add_head()

n = int(input())
commands = [input().rstrip() for _ in range(n)]

cur = linked_list.tail
for command in commands:
    print(command)
    is_tail = False
    if cur == linked_list.tail:
        is_tail = True

    is_head = False
    if cur == linked_list.head:
        is_head = True

    if command == "L":
        if is_head:
            continue
        cur = cur.pre
    elif command == "D":
        if is_tail:
            continue
        cur = cur.pos
    elif command == "B":
        if is_head:
            continue
        cur.pre.pos = cur.pos
        cur.pos.pre = cur.pre
        cur = cur.pre
        linked_list.size -= 1
    else:
        print(cur.char)
        char = command.split()[1]
        node = Node(char, cur, cur.pos)
        cur.pos = node
        cur = node
        print(cur.char)
        print(cur.pre.char)
        if is_tail:
            linked_list.tail = node

        if is_head:
            linked_list.head.pos.pre = node
            linked_list.head.pos = node
            node.pre = linked_list.head
        linked_list.size += 1
    linked_list.print_list()
