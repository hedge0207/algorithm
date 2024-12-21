def solution(want, number, discount):
    answer = 0
    items = {item:num for item, num in zip(want, number)}

    cart = {}
    for item in discount[:10]:
        if item not in cart:
            cart[item] = 1
        else:
            cart[item] += 1

    st = 0
    ed = 9
    while ed < len(discount)-1:
        item_removed = discount[st]
        if cart.get(item_removed):
            cart[item_removed] -= 1
            if cart[item_removed] == 0:
                cart.pop(item_removed)
        st += 1

        ed += 1
        item_added = discount[ed]
        if cart.get(item_added):
            cart[item_added] += 1
        else:
            cart[item_added] = 1

        if items == cart:
            answer += 1

    return answer