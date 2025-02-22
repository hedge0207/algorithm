def solution(n):
    greater_num = n+1
    num_one = bin(n).count("1")
    while 1:
        if num_one == bin(greater_num).count("1"):
            return greater_num
        greater_num += 1