def trap(height):
    stack = []
    trapped_rain = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if len(stack) == 0:
                break

            width = i - stack[-1] - 1
            depth = min(height[i], height[stack[-1]]) - height[top]
            trapped_rain += width * depth

        stack.append(i)
    return trapped_rain


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
