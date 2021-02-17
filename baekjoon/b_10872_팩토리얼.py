def factorial(k,n,fn):
    global result
    if k==n+1:
        result = fn
        return
    factorial(k+1,n,fn*k)

n = int(input())
result = 1
factorial(1,n,1)
print(result)