# 삽입 삭제가 번갈아가면서 빈번하게 이루어지는 경우 주로 힙을 쓴다.
# 완전 이진트리이어야 한다.
H = [0] * 100  # 힙
hsize = 0  # 힙에 저장된 자료의 수, stack의 탑 같이 마지막에 들어온 값의 인덱스


# 최소힙 구현(부모가 자식보다 작은 경우)

def push(item):  # 삽입
    global hsize
    hsize += 1
    H[hsize] = item  # 삽입하고
    c, p = hsize, hsize // 2
    while p and H[p] > H[c]:  # 부모가 자식보다 작아야 하므로 대소관계를 조정
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2


def mypop():  # 루트 삭제
    global hsize
    ret = H[1]  # H[1]은 루트
    H[1] = H[hsize]  # 마지막에 있는 노드(마지막 노드인 이유는 자식 노드가 없어서 이동이 편하기 때문)를 임시로 루트가 되게 한다.
    hsize -= 1
    p, c = 1, 2  #우선은 루트와 루트의 왼쪽 자식을 비교
    while c <= hsize:
        if c+1<=hsize and H[c]>H[c+1]: #c+1<=hsize는 오른쪽 자식이 있는지 체크하기 위함이다.
            c+=1        #c가 오른쪽 자식을 가리키게 한다
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            p = c
            c = p * 2  # c는 p의 왼쪽 자식 만일 위의 if문에서 결렸다면 오른쪽 자식
        else:
            break
    return ret


arr = [26, 29, 25, 22, 33, 37, 16, 15, 18]
for var in arr:
    push(var)

while hsize:
    print(mypop())
