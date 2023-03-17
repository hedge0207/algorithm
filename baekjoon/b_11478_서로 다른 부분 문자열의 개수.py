import sys

string = sys.stdin.readline().rstrip()
n = len(string)

sub_string = set()
for i in range(n):
    for j in range(i+1, n+1):
        sub_string.add(string[i:j])

print(len(sub_string))