N, K = map(int, input().split())

class Node:
    def __init__(self, num, prev=None, post=None):
        self.num = num
        self.post = post


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.cur = None

    def add_last(self, num):
        node = Node(num)
        if self.size == 0:
            self.head = node
        else:
            node.post = self.head
            self.cur.post = node

        self.size += 1
        self.cur = node

    def remove_node(self, prev_node):
        prev_node.post = self.cur.post
        if self.size == 1:
            print(self.cur.num, end="")
        else:
            print(self.cur.num, end=", ")
        self.cur = prev_node
        self.size -= 1

ll = LinkedList()
for i in range(1, N+1):
    ll.add_last(i)

cnt = 0
prev_node = ll.cur
ll.cur = ll.head
print("<", end="")
while ll.size != 0:
    cnt += 1
    if cnt == K:
        ll.remove_node(prev_node)
        cnt = 0
    prev_node = ll.cur
    ll.cur = ll.cur.post
print(">")



