def staircase(n):
    for i in range(n):
        stair = " " * (n-i-1) + "#" * (i+1)
        print(stair)