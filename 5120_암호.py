import sys
sys.stdin = open("5120_input.txt", "r")


class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


def cll(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        lst.head.prev.next=new
        new.next=lst.head
        new.prev=lst.head.prev
        lst.head.prev = new
    lst.size+=1

def add(lst):
    pre=None
    cur=lst.head
    for i in range(K):
        for i in range(M):
            pre=cur
            cur=cur.next
        new = Node(pre.data+cur.data)
        new.next=cur
        new.prev=pre
        cur.prev=new
        pre.next=new
        cur=new
        lst.size+=1


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    mylist = LinkedList()
    for i in arr:
        cll(mylist,Node(i))

    add(mylist)
    cur = mylist.head

    print("#{}".format(tc), end=" ")
    for i in range(mylist.size):
        if i>9:
            break
        cur = cur.prev
        print(cur.data, end=" ")
    print()