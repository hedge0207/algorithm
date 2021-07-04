num1, num2 = [int(num[::-1]) for num in input().split()]
if num1 > num2:
    print(num1)
else:
    print(num2)