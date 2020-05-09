import sys
sys.stdin = open("5110_input.txt", "r")


class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def addLast(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new


def myinsert(ml, num, new):
    if ml.head is None:
        ml.head = new.head
        ml.tail = new.tail

    else:
        pre = None
        cur = ml.head
        while cur is not None:
            if cur.data > num:
                break
            pre = cur
            cur = cur.next
        if cur is None:
            pre.next = new.head
            ml.tail = new.tail
        elif cur is ml.head:
            new.tail.next = ml.head
            ml.head = new.head
        else:
            pre.next = new.head
            new.tail.next = cur


def datalist(lst):
    cur = lst.head
    result = []
    while cur is not None:
        result += [cur.data]
        cur = cur.next
    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    l_list = LinkedList()
    for i in range(M):
        arr = list(map(int, input().split()))
        fir = arr[0]
        add_list = LinkedList()
        for j in arr:
            addLast(add_list, Node(j))
        myinsert(l_list, fir, add_list)
    result = datalist(l_list)
    print("#{}".format(tc), end=" ")
    for i in result[len(result):-11:-1]:
        print(i, end=" ")
    print()