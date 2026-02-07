n = int(input())
num_sell_book = {}
for _ in range(n):
    book = input()
    if num_sell_book.get(book):
        num_sell_book[book] += 1
    else:
        num_sell_book[book] = 1

best_seller = ""
max_sell = 0
for book, num_sell in num_sell_book.items():
    if num_sell > max_sell:
        best_seller = book
        max_sell = num_sell
    elif num_sell == max_sell:
        if best_seller > book:
            best_seller = book
print(best_seller)
