# 3/16(월) APS 기본 수업
p = "banana"
t = "qweqwbananaegrgrghfbdbsgaaaaasdgswetwegw"
n, m = len(t), len(p)

# skip 테이블 생성
skip = [m] * 128  # 아스키 코드값으로 a~z, A~Z는 0~128 사이이므로 128로 설정

for i in range(m - 1):  # 마지막 문자는 굳이 할 필요가 없다
    skip[ord(p[i])] = m - 1 - i

i = 0
while i <= n - m:
    for j in range(m - 1, -1, -1):
        if p[j] != t[i + j]:
            i += skip[ord(t[i + m - 1])]
            break
    else:
        print(i)
        i += m
