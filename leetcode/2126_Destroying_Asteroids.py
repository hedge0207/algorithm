class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass - asteroid < 0:
                return False
            mass += asteroid
        return True