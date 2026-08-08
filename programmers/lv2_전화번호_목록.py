def solution(phone_book):
    prefix_set = set()
    for number in phone_book:
        prefix = ""
        for i in range(len(number)-1):
            digit = number[i]
            prefix += digit
            prefix_set.add(prefix)

    for number in phone_book:
        if number in prefix_set:
            return False
    return True



# best_practice
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True