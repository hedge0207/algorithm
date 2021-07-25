h, m = map(int, input().split())
EM = 45

flag = False
if m - EM < 0:
    m = 60 - abs(m - EM)
    flag = True
else:
    m = m - EM

if flag:
    h = h - 1
    if h < 0:
        h = 23

print(h, m)
