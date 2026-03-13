dna = input()

ans = 0
st = 0
for ed in range(len(dna)):
    if dna[st] != dna[ed]:
        ans = max(ans, ed - st)
        st = ed
print(max(ans, len(dna)-st))