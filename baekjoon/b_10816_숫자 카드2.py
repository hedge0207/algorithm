import sys


def lower_bound(num):
    st, ed = 0, num_cards
    while st < ed:
        mid = (st+ed) // 2
        if cards[mid] >= num:
            ed = mid
        else:
            st = mid + 1
    return st

def upper_bound(num):
    st, ed = 0, num_cards
    while st < ed:
        mid = (st+ed) // 2
        if cards[mid] > num:
            ed = mid
        else:
            st = mid + 1
    return st


input = sys.stdin.readline
_ = input()
cards = sorted(list(map(int, input().split())))
_ = input()
nums = list(map(int, input().split()))
num_cards = len(cards)

for num in nums:
    print(upper_bound(num) - lower_bound(num), end=" ")
