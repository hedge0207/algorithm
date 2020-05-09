# 유클리드 알고리즘으로 최대공약수 구하기(모두의 알고리즘 p.62)
# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다.
# 또한 어떤 수와 0의 최대공약수는 자기 자신이다.
# def gdc(a, b):
#     print(b)
#     if b == 0:
#         return a
#     return gdc(b, a % b)
#
#
# print(gdc(60,24))
# print(gdc(81,27))


# 피보나치 수열 구하기
# def fibo(n):
#     if n < 2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
#
# print(fibo(4))

# 하노이의 탑

# def hanoi(disks, st, ed):
#     if disks == 0:
#         return
#     ot = 6 - st - ed
#     hanoi(disks - 1, st, ot)
#     print("{}번 원판을 {}번 기둥에서 {}번 기둥으로 이동".format(disks, st, ed))
#     hanoi(disks - 1, ot, ed)
#
# hanoi(3, 1, 3)
#결국 하노이 탑 문제를 푸는 순서는 아래와 같다.
# 첫 번째로 n-1개 일 때 하노이탑 문제 풀기(1번 기둥에서 2번 기둥으로 가장 넓은 원반을 제외한 모든 원반을 옮기기),
# 두 번째로 가장 큰 원반을 3번 기둥으로 옮기기
# 세 번째로 n-1개 일 때 하노이탑 문제 풀기(2번 기둥에서 3번 기둥으로 가장 넓은 원반을 제외한 모든 원반을 옮기기)
# 따라서 원반을 옮기는 총 횟수는 (원반의 개수가 n-1일때 원반을 총 옮기는 횟수)*2(2번 하므로)+1(가장 큰 원반을 옮기는 횟수)
# 결국 첫 번째, 세 번째 순서에서 더 작은 수준의 문제를 풀어야 하므로 재귀적인 문제라고 할 수 있다.


#정올 1309
# def f(n):
#     if n < 2:
#         print("{}! = {}".format(n, n))
#         return 1
#     print("{}! = {} * {}!".format(n,n,n-1))
#     return n*f(n-1)
#
# print(f(int(input())))


# 정올 1169

 #이전에 선택한 요소들에 대한 정보

def backtrack(k):       #k는 함수 호출 트리의 높이, 선택한 요소의 수
    if k == N:          #단말노드의 도착, 모든 선택이 끝났다. 여기까지 오면 order에 하나의 순열이 저장된다.
        print(order)
    else:               #아직 해야할 선택이 남은 상태
        for i in range(N):
            if visit[i]:            #32~34번줄이 없을 경우 중복순열이 출력됨
                continue
            visit[i] = 1
            order.append(arr[i])
            backtrack(k+1)
            order.pop()
            visit[i] = 0    #다른 루트로 갈 수 있도록 0으로 초기화
backtrack(0)


def f(k,n,m):
    global order
    if k == n:
        print(order)
    else:
        for i in range(n):
            if visit[i]:
                continue
            visit[i] = 1
            order+=

n,m = map(int,input().split())
order = ""
visit = [0]*n

f(0,n,m)
