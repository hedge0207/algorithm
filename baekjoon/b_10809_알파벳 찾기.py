word = input()

c = 97
alpha_dict = {}
for _ in range(26):
    alpha_dict[chr(c)]=-1
    c += 1

cnt = 1
for i in word:
    if alpha_dict[i] == -1:
        alpha_dict[i]+=cnt
    cnt+=1

for i in alpha_dict:
    print(alpha_dict[i],end=" ")