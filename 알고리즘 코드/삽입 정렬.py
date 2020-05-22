arr = [10,2,4,8,79,5,43,77,22,4]
N= len(arr)

for i in range(1,N): #i는 정렬된 집합과 정렬되지 않은 집합의 경계를 나타내게 된다.
    tmp=arr[i]   #삽입할 원소
    j=i-1
    while j>=0 and arr[j]>tmp:
        arr[j+1]=arr[j]
        print(arr)
        j-=1
    arr[j+1]=tmp
    print(arr)

print(arr)