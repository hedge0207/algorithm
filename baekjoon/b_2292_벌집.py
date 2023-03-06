N = int(input())
max_room_number = 1
result = 1
while max_room_number < N:
    max_room_number = max_room_number + (6 * result)
    result += 1

print(result)