def prime_factors(n):
    factorized_int = {}
    while 1:
        for i in range(2, n):
            if n % i == 0:
                if factorized_int.get(i):
                    factorized_int[i] += 1
                else:
                    factorized_int[i] = 1
                n //= i
                break
        else:
            if factorized_int.get(n):
                factorized_int[n] += 1
            else:
                factorized_int[n] = 1
            break

    result = ""
    for num, squared in factorized_int.items():
        if squared > 1:
            result += "({}**{})".format(num, squared)
        else:
            result += "({})".format(num)
    return result
