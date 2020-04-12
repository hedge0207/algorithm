import sys
sys.stdin = open("5122_input.txt", "r")

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

def myPop(ml, idx):
    if ml.head is None:
        return
    elif ml.head.next is None:
        ml.tail = None
    elif idx == 0:
        ml.head = ml.head.next
    elif idx >= ml.size:
        pre = None
        cur = ml.head
        while cur.next is not None:
            pre = cur
            cur = cur.next
        pre.next = None
        ml.tail = pre
    else:
        pre = None
        cur = ml.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
    ml.size -= 1

def change(ml, idx, num):
    if ml.head is None:
        return
    cur=ml.head
    for _ in range(idx):
        cur=cur.next
    cur.data=num

def findL(ml, l):
    cur = ml.head
    flag=0
    for _ in range(l):
        if cur.next is None:
            return -1
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
        edit = list(input().split())
        if len(edit) == 2:
            myPop(mylist, int(edit[1]))
        elif edit[0] == "I":
            myInsert(mylist, int(edit[1]), Node(int(edit[2])))
        else:
            change(mylist, int(edit[1]), int(edit[2]))
    print("#{} {}".format(tc, findL(mylist, L)))




# list
# T = int(input())
# for tc in range(1,T+1):
#     N,M,L= map(int,input().split())
#     arr = list(map(int, input().split()))
#     for i in range(M):
#         a = list(input().split())
#         if len(a)==2:
#             arr.pop(int(a[1]))
#         else:
#             if a[0]=="I":
#                 arr.insert(int(a[1]),int(a[2]))
#             else:
#                 arr[int(a[1])]=int(a[2])
#
#     if len(arr)>L:
#         print("#{} {}".format(tc,arr[L]))
#     else:
#         print("#{} -1".format(tc))
