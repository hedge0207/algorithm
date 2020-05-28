# 노드의 개수 13
# 간선: 1 2 1 3 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''
6
1 2 1 3 2 4 2 5 3 6
'''


V = int(input())
E = V-1
arr = list(map(int,input().split()))
L = [0]*(V+1)
R = [0]*(V+1)
P = [0]*(V+1)



for i in range(0,len(arr),2):
    parent,child = arr[i],arr[i+1]
    if L[parent]:      # 만일 왼쪽 자식 노드가 이미 있으면(자식 노드는 왼쪽부터 이므로)
        R[parent]=child # 오른쪽 자식 노드 추가
    else:      #없으면
        L[parent]=child  #왼쪽 자식 노드부터 추가
    P[child]=parent  #부모 노드에 대한 정보 추가

print(L)
print(R)
print(P)

# def inorder(v): #v: 방문하는 노드 번호
#     if v==0:
#         return
#
#     #전위순회
#     print(v, end=" ")
#     inorder(L[v])
#     inorder(R[v])
# inorder(6)

def inorder(v):
    if v == 0: #자식 노드가 0이라는 건 자식이 존재하지 않는다는 것이므로 return
        return

    # 중위순회
    inorder(L[v])  #자식 노드를 타고 가면서 순회
    print(v, end=" ")
    inorder(R[v])
inorder(6)
# def inorder(v):
#     if v == 0:
#         return
#
#     # 후위순회
#     inorder(L[v])
#     inorder(R[v])
#     print(v, end=" ")