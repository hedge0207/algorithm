def high_and_low(numbers):
    numbers = list(map(int, numbers.split(" ")))
    answer = "{} {}".format(max(numbers), min(numbers))

    return answer



print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))