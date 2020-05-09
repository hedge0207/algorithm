import sys

sys.stdin = open("4552_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    text = input()
    n = len(text)

    if n == 1:
        print("#{} Exist".format(tc))
    else:
        i = 0
        j = n - 1
        while True:
            if text[i] == text[j] or text[i] == "?" or text[j] == "?":
                i += 1
                j -= 1
                if i == n // 2:
                    print("#{} Exist".format(tc))
                    break

            else:
                print("#{} Not exist".format(tc))
                break