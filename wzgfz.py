arr = [12,3,4,8,4,8,3,2,1,5,484,9]

def q(lo,hi):
    if lo>=hi:
        return
    i,j=lo,hi
    while i<j:
        while i<=hi and arr[lo]>=arr[i]:
            i+=1
        while arr[lo]<arr[j]:
            j-=1
        if i>=j:
            break
        arr[i],arr[j]=arr[j],arr[i]
    arr[lo],arr[j]=arr[j],arr[lo]
    q(lo,j-1)
    q(j+1,hi)

q(0,len(arr)-1)
print(arr)
