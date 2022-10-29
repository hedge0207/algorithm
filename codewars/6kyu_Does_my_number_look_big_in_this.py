def is_narcissistic_number(number):
    number = str(number)
    n = len(number)
    result = sum(int(digit) ** n for digit in number)
    if str(result) == number:
        return True
    return False
