def fibonacci(k,n,num1,num2):
    global result
    if k==n-1:
        result = num2
        return
    fibonacci(k+1,n,num2,num1+num2)

n = int(input())
if n:
    result = 0
    fibonacci(0,n,0,1)
    print(result)
else:
    print(0)