string = input()

exps = string.split("-")
ans = sum(list(map(int, exps[0].split("+"))))


for i in range(1, len(exps)):
    ans -= sum(list(map(int, exps[i].split("+"))))

print(ans)