phone_num_a = input()
phone_num_b = input()

all_num = ""
for i in range(8):
    all_num += phone_num_a[i]
    all_num += phone_num_b[i]

while len(all_num) != 2:
    nums = ""
    for i in range(len(all_num)-1):
        nums += str(int(all_num[i]) + int(all_num[i+1]))[-1]
    all_num = nums

print(all_num)