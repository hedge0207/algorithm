def solution(rows, columns, queries):
    answer = []
    table = []
    num = 1
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(num)
            num += 1
        table.append(row)

    for query in queries:
        new_table = [row[:] for row in table]
        min_num = 10000
        x1, y1, x2, y2 = list(map(lambda x: x-1, query))
        for i in range(y1+1, y2+1):
            new_table[x1][i] = table[x1][i-1]
            min_num = min(min_num, table[x1][i-1])

        for i in range(x1+1, x2+1):
            new_table[i][y2] = table[i-1][y2]
            min_num = min(min_num, table[i-1][y2])

        for i in range(y1 ,y2):
            new_table[x2][i] = table[x2][i+1]
            min_num = min(min_num, table[x2][i+1])

        for i in range(x1, x2):
            new_table[i][y1] = table[i+1][y1]
            min_num = min(min_num, table[i+1][y1])

        table = new_table
        answer.append(min_num)

    return answer




































print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))