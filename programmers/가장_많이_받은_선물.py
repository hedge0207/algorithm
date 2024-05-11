def solution(friends, gifts):
    answer = 0

    gift_scores = {friend: 0 for friend in friends}
    gift_log = {sender: {receiver: 0 for receiver in friends} for sender in friends}

    for gift in gifts:
        sender, receiver = gift.split()
        gift_scores[sender] += 1
        gift_scores[receiver] -= 1
        gift_log[sender][receiver] += 1

    n = len(friends)
    for i in range(n):
        sender = friends[i]
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            receiver = friends[j]

            if gift_log[sender][receiver] == gift_log[receiver][sender]:
                if gift_scores[sender] > gift_scores[receiver]:
                    cnt += 1
            elif gift_log[sender][receiver] > gift_log[receiver][sender]:
                cnt += 1
        answer = max(cnt, answer)
    return answer


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
solution(friends, gifts)
