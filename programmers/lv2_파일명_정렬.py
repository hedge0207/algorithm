def solution(files):
    n = len(files)
    split_files = []
    for i in range(n):
        head = ""
        number = ""
        file = files[i].lower()
        for char in file:
            if len(number) != 0 and not char.isdigit():
                break
            if char.isdigit():
                number += char
            else:
                head += char
        split_files.append([head, int(number), i])

    split_files.sort(key=lambda x:(x[0], x[1], x[2]))

    ans = []
    for split_file in split_files:
        ans.append(files[split_file[2]])
    return ans