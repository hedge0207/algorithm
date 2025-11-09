n = int(input())
if n <= 2:
    print(n)
else:
    post_1 = 1
    post_2 = 2
    ans = post_1
    for _ in range(2, n):
         ans = (post_1 + post_2) % 15746
         post_1 = post_2
         post_2 = ans
    print(ans % 15746)