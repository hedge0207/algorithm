class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance_x = abs(z-x)
        distance_y = abs(z-y)
        if distance_x > distance_y:
            return 2
        elif distance_y > distance_x:
            return 1
        else:
            return 0
