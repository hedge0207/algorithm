def convert_to_minute(time: str):
    hour, minute = map(int, time.split(":"))
    return minute + hour * 60

def solution(plans):
    for plan in plans:
        plan[1] = convert_to_minute(plan[1])
        plan[2] = int(plan[2])
    plans.sort(key=lambda x:x[1], reverse=True)

    remains = []
    answer = []
    while len(plans) > 1:
        plan = plans.pop()
        interval = plans[-1][1] - plan[1]

        if interval < plan[2]:
            plan[2] -= interval
            remains.append(plan)
        else:
            answer.append(plan[0])
            interval -= plan[2]
            while remains and interval > 0:
                remain = remains.pop()
                interval = interval - remain[2]
                if interval < 0:
                    remain[2] = -interval
                    remains.append(remain)
                else:
                    answer.append(remain[0])

    return answer + [plan[0] for plan in plans] + [remain[0] for remain in remains[::-1]]