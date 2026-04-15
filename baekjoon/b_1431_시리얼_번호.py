def sort_serial_number(serial_number):
    length = len(serial_number)
    sum_ = 0
    for char in serial_number:
        if char.isdigit():
            sum_ += int(char)
    return [length, sum_, serial_number]

n = int(input())
for serial_number in sorted([input() for _ in range(n)], key=sort_serial_number):
    print(serial_number)