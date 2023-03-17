import sys

input = sys.stdin.readline
start, end, final = map(lambda x: int("".join(x.split(":"))), input().split())
participants = {}
result = 0

while True:
    try:
        timestamp, name = input().split()
        timestamp = int("".join(timestamp.split(":")))
        if name in participants and participants[name] != "verified":
            if participants[name] <= start and end <= timestamp <= final:
                result += 1
                participants[name] = "verified"
        else:
            participants[name] = timestamp
    except:
        break

print(result)
