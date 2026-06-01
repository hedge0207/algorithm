n = int(input())
student_numbers = [input() for _ in range(n)]
ans = 1
while ans <= len(student_numbers[0]):
    unique_numbers = set()
    for student_number in student_numbers:
        new_number = student_number[len(student_number)-ans:]
        if new_number in unique_numbers:
            break
        unique_numbers.add(new_number)
    else:
        break
    ans += 1
print(ans)