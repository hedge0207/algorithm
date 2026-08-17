def solution(progresses, speeds):
    answer = []
    arr = []
    for progress, speed in zip(progresses, speeds):
        remain = int((100-progress) / speed)
        if progress + remain * speed < 100:
            remain += 1
        if len(arr) == 0:
            arr.append(remain)
            continue
        if remain > arr[0]:
            answer.append(len(arr))
            arr = [remain]
        else:
            arr.append(remain)
    if arr:
        answer.append(len(arr))
    return answer