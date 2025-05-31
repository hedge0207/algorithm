def solution(users, emoticons):
    discount_rates = [0.1, 0.2, 0.3, 0.4]
    max_num_sum_users = 0
    max_amount = 0

    def recur(d, rates):
        nonlocal max_amount, max_num_sum_users
        if d == len(emoticons):
            amounts_per_user = {}
            num_sub_users = 0
            total_amount = 0
            for i, user in enumerate(users):
                acceptable_rate, limit = user
                amounts_per_user[i] = 0
                acceptable_rate /= 100
                for rate, price in zip(rates, emoticons):
                    if rate >= acceptable_rate:
                        amounts_per_user[i] += price - (price * rate)

                    if amounts_per_user[i] >= limit:
                        num_sub_users += 1
                        amounts_per_user[i] = 0
                        break
                total_amount += amounts_per_user[i]
            if max_num_sum_users < num_sub_users:
                max_num_sum_users = num_sub_users
                max_amount = total_amount
            elif max_num_sum_users == num_sub_users:
                if max_amount < total_amount:
                    max_amount = total_amount
            return

        for i in range(d, len(emoticons)):
            for discount_rate in discount_rates:
                rates.append(discount_rate)
                recur(i+1, rates)
                rates.pop()

    recur(0, [])
    return [max_num_sum_users, int(max_amount)]































solution([[40, 10000], [25, 10000]], [7000, 9000])
solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])