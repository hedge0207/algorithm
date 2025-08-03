def change_switches_multiple_of_num(num):
    multiple = 1
    while num * multiple <= num_switches:
        switches[num * multiple] = 1 - switches[num * multiple]
        multiple += 1

def change_switches_in_symmetry_range(num):
    st = num - 1
    ed = num + 1
    switches[num] = 1 - switches[num]
    while st > 0 and ed <= num_switches:
        if switches[st] != switches[ed]:
            break
        switches[st] = 1 - switches[st]
        switches[ed] = 1 - switches[ed]
        st -= 1
        ed += 1

num_switches = int(input())
switches = [0] + list(map(int, input().split()))
num_commands = int(input())
commands = [list(map(int, input().split())) for _ in range(num_commands)]

for command_type, num in commands:
    if command_type == 1:
        change_switches_multiple_of_num(num)
    else:
        change_switches_in_symmetry_range(num)

for i in range(1, num_switches + 1):
    print(switches[i], end=" ")
    if i  % 20 == 0:
        print()











"""
63
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1
1 1
"""