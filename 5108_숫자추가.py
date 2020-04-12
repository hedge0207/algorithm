import sys

sys.stdin = open("5108_input.txt", "r")


# linked list
class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n


class ML:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def myInsert(ml, idx, new):
    if ml.head is None:
        ml.head = ml.tail = new
    elif idx == 0:
        new.next = ml.head
        ml.head = new
    elif idx >= ml.size:
        ml.tail.next = new
        ml.tail = new
    else:
        pre = None
        cur = ml.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = new
        new.next = cur
    ml.size += 1


def findL(ml, l):
    cur = ml.head
    for _ in range(l):
        cur = cur.next

    return cur.data


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    mylist = ML()
    for i in arr:
        myInsert(mylist, len(arr), Node(i))
    for i in range(M):
        index, number = map(int, input().split())
        myInsert(mylist, index, Node(number))
    print("#{} {}".format(tc, findL(mylist, L)))

# list
# T = int(input())
# for tc in range(1,T+1):
#     N,M,L = map(int, input().split())
#     arr = list(map(int,input().split()))
#     for i in range(M):
#         index,number = map(int,input().split())
#         arr.insert(index,number)
#
#     print("#{} {}".format(tc,arr[L]))