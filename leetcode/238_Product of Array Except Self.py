"""
제약조건
- O(n)안에 풀 것
- 나눗셈을 사용하지 않을 것
"""
def productExceptSelf(nums):
    left = [nums[0]]
    right = [nums[-1]]
    
    # 왼쪽과 오른쪽의 곱을 미리 구해두고
    for i in range(1, len(nums)):
        left.append(left[i - 1] * nums[i])
        right = [right[0] * nums[-i - 1]] + right

    # 위해서 구한 왼쪽과 오른쪽의 곱을 이용해서 결과 값을 구한다.
    result = []
    for i in range(len(nums)):
        if i == 0:
            ans = right[i + 1]
        elif i == len(nums) - 1:
            ans = left[i - 1]
        else:
            ans = left[i - 1] * right[i + 1]
        result.append(ans)

    return result

"""
best practice
위 방식으로도 풀리긴하지만 공간복잡도가 O(n)이다.
아래와 같이 풀면 공간복잡도 O(1)로 풀 수 있다.     
"""
def productExceptSelf(nums):
    result = []
    multiply = 1
    for i in range(len(nums)):
        result.append(multiply)
        multiply *= nums[i]

    multiply = 1
    for i in range(len(nums)-1, -1, -1):
        print(i)
        result[i] = result[i] * multiply
        multiply *= nums[i]

    return result