#중첩된 for문으로 생성하기
arr = "ABC"
N = len(arr)

#가장 원시작인 방법(중복을 포함)
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(arr[i],arr[j],arr[k])
            
            
#가장 원시작인 방법(중복 미포함)
# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         for k in range(N):
#             if k==i or k ==j:
#                 continue
#             print(arr[i],arr[j],arr[k])

#아래와 같이 하면 제대로 작동하지 않는다.
# result = []
# for i in range(N):
#     result.append(arr[i])
#     for j in range(N):
#         if arr[j] in result:
#             continue
#         result.append(arr[j])
#         for k in range(N):
#             if arr[k] in result:
#                 continue
#             result.append(arr[k])
#
#             print(result)

#아래와 같이 해야 제대로 출력된다. 재귀로 구하는 것과 동일한 방법이다.
# result = []
# for i in range(N):
#     result.append(arr[i])
#     for j in range(N):
#         if arr[j] in result:
#             continue
#         result.append(arr[j])
#         for k in range(N):
#             if arr[k] in result:
#                 continue
#             result.append(arr[k])
#
#             print(result)
#
#             result.pop()
#         result.pop()
#     result.pop()

#인덱스 기반으로 체크, 재귀호출과 똑같은 방식
# visit = [0]*N
# result=[]
# for i in range(N):
#     result.append(arr[i])
#     visit[i]=1
#     for j in range(N):
#         if visit[j]:
#             continue
#         result.append(arr[j])
#         visit[j] = 1
#         for k in range(N):
#             if visit[k]:
#                 continue
#             result.append(arr[k])
#             visit[k] = 1
#
#             print(result)
#
#             result.pop()
#             visit[k] = 0
#         result.pop()
#         visit[j] = 0
#     result.pop()
#     visit[i] = 0


#재귀를 사용한 순열
def perm(n,k):
    if n==k:
        print(a)
    else:
        for i in range(k,n):
            a[i],a[k]=a[k],a[i]
            perm(n,k+1)
            a[k],a[i]=a[i],a[k]
a = [1,2,3]
perm(3,0)