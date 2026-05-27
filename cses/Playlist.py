n = int(input())
songs = list(input().split())
ans = 0
idx_per_song = {}
st = 0
for i in range(n):
    song = songs[i]
    if song in idx_per_song:
        st = max(st, idx_per_song[song]+1)
    idx_per_song[song] = i
    ans = max(ans, i-st+1)
print(ans)