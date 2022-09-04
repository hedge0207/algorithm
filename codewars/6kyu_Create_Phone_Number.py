def create_phone_number(n):
    result = "("
    for i in range(len(n)):
        if i == 3:
            result += ") "
        if i == 6:
            result += "-"
        result += str(n[i])
    return result


sample_tests = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"],
    [[0, 2, 3, 0, 5, 6, 0, 8, 9, 0], "(023) 056-0890"],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "(000) 000-0000"]
]

for nums, result in sample_tests:
    print(result == create_phone_number(nums))



"""
best practice

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

"""