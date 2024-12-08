def solution(storey):
    ans = 0
    power = 0
    while 1:
        quotient = storey // 10 ** power % 10
        if power > len(str(storey)):
            break
        if quotient > 5:
            stares = 10 - quotient
            storey += stares * 10 ** (power)
        elif quotient == 5:
            if storey // 10 ** (power + 1) % 10 >= 5:
                stares = 10 - quotient
                storey += stares * 10 ** (power)
            else:
                stares = quotient
                storey -= stares * 10 ** (power)
        else:
            stares = quotient
            storey -= stares * 10 ** (power)

        ans += stares
        power += 1
    return ans