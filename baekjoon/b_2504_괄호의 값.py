def rec(k,n):
    stack.push(bracket[k])
    rec(k+1,n)
    stack.pop()



bracket = list(input())
if bracket.count('(')==bracket.count(')') and bracket.count('[')==bracket.count(']'):
    stack = []
    result = 0
    rec(0,len(bracket))
    print(result)
else:
    print(0)




