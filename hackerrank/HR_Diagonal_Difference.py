def diagonalDifference(arr):
    n = len(arr)
    top_right = 0
    top_left = 0
    for i in range(n):
        top_right += arr[i][i]
        top_left += arr[i][n-i-1]
    return abs(top_right-top_left)