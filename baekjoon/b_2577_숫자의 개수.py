num1,num2,num3 = int(input()),int(input()),int(input())
num = num1*num2*num3

num_dict = {}

for i in range(10):
    num_dict[i]=0

for i in str(num):
    num_dict[int(i)]+=1

for k in num_dict:
    print(num_dict[k])
