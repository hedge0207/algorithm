s = int(input())

num = 1
sum_ = 0
cnt = 0
while sum_ < s:
    sum_ += num
    num += 1
    cnt += 1

if sum_ == s:
    print(cnt)
else:
    print(cnt-1)