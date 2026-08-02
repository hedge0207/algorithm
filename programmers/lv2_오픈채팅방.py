def solution(record):
    final_nickname = {}
    for log in record:
        splitted = log.split()
        if len(splitted) == 3:
            final_nickname[splitted[1]] = splitted[2]
    answer = []
    for log in record:
        splitted = log.split()
        if splitted[0] == "Enter":
            answer.append(f"{final_nickname[splitted[1]]}님이 들어왔습니다.")
        elif splitted[0] == "Leave":
            answer.append(f"{final_nickname[splitted[1]]}님이 나갔습니다.")

    return answer