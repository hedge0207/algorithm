#집합을 생성하는 함수
def make_set(x):
    p[x]=x

#집합의 대표자를 찾는 함수
def find_set(x):
    if p[x]==x:     #부모가 자기 자신이면 루트라는 뜻이므로
        return x    #자신을 리턴
    else:
        return find_set(p[x])  #아니면 부모 노드로 이동

#두 집합 중 한 집합의 대표자가 다른 집합의 대표자의 부모가 되면 두 집합이 합쳐진다.
#x가 속한 집합과 y가 속한 집합이 합쳐지고 x가 대표자가 된다.
def union(x,y):
    p[find_set(y)]=find_set(x)


N = 6
p = [0]*(N+1)
for i in range(1,N+1):
    make_set(i)

union(1,3)
union(2,3)
union(5,6)
print(p)
print(find_set(6))



#rank
def make_set(x):
    p[x]=x

def find_set(x):
    if p[x]==x:
        return x
    else:
        p[x]=find_set(p[x]) #부모 노드를 대표자로 갱신, path compresion
        return p[x]         #최초 인자로 들어온 x에서 대표자까지 가는 재귀를 거치면서 경로상에 있는 모든 노드의 부모 노드가 대표자가 됨

def union(x,y):
    px = find_set(x) #px는 x의 대표자
    py = find_set(y) #py는 y의 대표자
    if rank[px]>rank[py]:   #px의 깊이가 py의 길이보다 크면
        p[py]=px            #px가 대표가 된다.
    else:                   #py의 깊이가 길거나 둘의 깊이가 같으면
        p[px]=py            #py가 대표가 된다.
        if rank[px]==rank[py]:  #만일 둘의 깊이가 같으면
            rank[py]+=1         #대표가 된 py의 깊이에 +1을 해준다.

N = 8
p = [0]*(N+1)
rank = [0]*(N+1)  #트리의 깊이를 저장하는 배열
for i in range(1,N+1):
    make_set(i)

union(1,3)
union(2,3)
union(5,6)
union(6,8)
union(1,5)
union(6,7)
print(p)
print(find_set(4))
print(find_set(5))