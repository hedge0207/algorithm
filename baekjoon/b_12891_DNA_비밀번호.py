S, P = map(int, input().split())
string = input()
DNA_CHARS = ["A", "C", "G", "T"]

MIN_NUM = {}
for char, min_num in zip(DNA_CHARS, map(int, input().split())):
    MIN_NUM[char] = min_num

ans = 0
st = 0
ed = st + P - 1
appearance = {dna_char:0 for dna_char in DNA_CHARS}
for char in string[st:ed + 1]:
    appearance[char] += 1

while 1:
    for dna_char in DNA_CHARS:
        if appearance[dna_char] < MIN_NUM.get(dna_char):
            break
    else:
        ans += 1
    appearance[string[st]] -= 1
    st += 1
    ed += 1
    if ed == S:
        break
    appearance[string[ed]] += 1


print(ans)