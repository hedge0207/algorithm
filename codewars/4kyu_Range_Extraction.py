def solution(args):
    args.sort()
    ans = ""
    st = 0
    for i in range(1, len(args)):
        if args[i]-1 != args[i-1]:
            if i - st <= 2:
                ans += str(args[st]) + ","
                if i - st == 2:
                    ans += str(args[st+1]) + ","
            else:
                ans += f"{args[st]}-{args[i-1]},"
            st = i
    if len(args)-st <= 2:
        if len(args)-st == 2:
            ans += f"{args[st]},{args[st + 1]}"
        else:
            ans += f"{args[st]}"
    else:
        ans += f"{args[st]}-{args[len(args) - 1]}"
    return ans