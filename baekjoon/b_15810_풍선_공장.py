n, m = map(int, input().split())
staffs = list(map(int, input().split()))

def binary_search(num_balloons):
    l, r = 0, min(staffs) * num_balloons
    while l < r:
        m = (l+r) // 2
        completed = sum([m // staff for staff in staffs])
        if num_balloons > completed:
            l = m + 1
        elif num_balloons <= completed:
            r = m
    return l

print(binary_search(m))