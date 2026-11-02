def miniMaxSum(arr):
    arr.sort()
    sum_ = sum(arr)
    print(sum_ - arr[-1], sum_ - arr[0])