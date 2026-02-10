n, m = map(int, input().split())
trees = list(map(int, input().split()))

st, ed = 0, max(trees)
while st <= ed:
    mid = (st+ed) // 2
    woods = sum([tree-mid for tree in trees if tree-mid > 0])
    if woods >= m:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)