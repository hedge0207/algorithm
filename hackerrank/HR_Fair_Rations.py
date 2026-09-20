def fairRations(B):
    carry = 0
    ans = 0

    for i in range(len(B)-1):
        if (B[i] + carry) % 2 == 1:
            ans += 2
            carry = 1
        else:
            carry = 0

    if (B[-1] + carry) % 2 == 1:
        return "NO"
    else:
        return ans