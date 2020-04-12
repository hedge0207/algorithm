import sys
sys.stdin = open("1928_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    base64 = input()

    asd = []
    for i in base64:
        if "A" <= i <= "Z":
            asd.append(ord(i)-ord("A"))
        elif "a" <= i <= "z":
            asd.append(ord(i)-ord("a")+26)
        elif "0" <= i <= "9":
            asd.append(int(i)+52)
        elif i == "+":
            asd.append(62)
        elif i =="/":
            asd.append(63)

    arr = []
    for i in asd:
        arrr = ""
        while i != 0:
            arrr += str(i % 2)
            i //= 2
        while len(arrr) !=6:
            arrr += "0"
        rrra = reversed(arrr)
        arr += rrra

    bit_8 = [[0]*8 for _ in range(len(arr)//8)]
    c = -1
    for i in range(len(arr)//8):
        for j in range(8):
            c += 1
            bit_8[i][j] = arr[c]


    asc = []
    for i in range(len(bit_8)):
        e = 0
        d = 8
        for j in range(8):
            d -= 1
            if bit_8[i][j] == "1":
                e += 2**d
        asc.append(e)

    sol = ""
    for i in asc:
        sol += chr(i)

    print("#{} {}".format(tc,sol))





