N = int(input())
max_length = 2*N-1

for i in range(1, N+1):
    num_starts = 2*i-1
    empty_space = (max_length-num_starts)//2
    print(" "*empty_space, end="")
    print("*"*num_starts)